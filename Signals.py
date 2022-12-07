# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:26:58 2022

@author: Ortíz Montúfar Gerardo
"""
from numpy import array, transpose, iinfo, int16, linspace
from scipy.signal import lfilter
from scipy.io import loadmat, savemat, wavfile
import json
from scipy.fft import fft
from scipy.interpolate import PchipInterpolator, Akima1DInterpolator, CubicSpline, InterpolatedUnivariateSpline
from Filters import Filter

class RegistryError(Exception):
    def __init__(self):
        super().__init__("You must check the registry. It could contain a wrong data")


class SignalFile:
    def __init__(self,filename, action, data = {}):
        
        self.action = action
        self.name = filename
        self.extention = self.name[self.name.find('.') + 1:]
        self.data = data
        
    def Gen(self):
        if self.action == 'r':
            methods = {
                'wav' : self.ReadWav,
                'mat' : self.ReadMat,
                'txt' : self.ReadTxt,
                'csv' : self.ReadTxt,
                'json' : self.ReadJSON
                }
            
        elif self.action == 'w':
            methods = {
                'wav' : self.WriteWav,
                'mat' : self.WriteMat,
                'txt' : self.WriteTxt,
                'csv' : self.WriteTxt,
                'json' : self.WriteJSON
                }
            
        else:
            raise NameError('Error: only acept "r" or "w"')
        
        accion = methods[self.extention]
        data = accion()
        
        return data
                
        
    def ReadWav(self):
        fs, data = wavfile.read(self.name)
        try:
            content = [data[:,0],data[:,1]]
            content = {'fs': fs, self.name : content}
        except Exception:
            content = data
            content = {'fs': fs, self.name : content}
            
        return content
        
    def ReadMat(self):
        content = loadmat(self.name, squeeze_me = True)
        inservible = ['__header__','__globals__','__version__']
        for key in inservible:
            content.pop(key)
        
        try:
            for key in content:
                content[key] = content[key]
                
            content['fs'] = int(content['fs'])
            
        except Exception:
            pass
        
        return content
    
    def ReadTxt(self):
        archivo = open(self.name, 'r')
        datos, keys, i, flagError = [], [], 1, False
        
        for linea in archivo:
            l = linea.replace(',',' ')
            l, nl = l.split() ,[]
            
            for dato in l:
                try:
                    aux = float(dato)
                    
                except ValueError:
                    keys.append(dato)
                    if i > 1:
                        print("Error: There's a string in your register '{}' in line {}".format(dato,i))
                        flagError = True
                else:
                    nl.append(aux)
            
            if len(nl) > 0:        
                datos.append(nl)
            i += 1
        
        content = array(datos)
        
        if flagError:
            raise RegistryError
        
        info, i = {}, 0
        for key in keys:
            info[key] = transpose(content)[i]
            i += 1
        if info == {}:
            content = transpose(content)
            for i in range(len(content)):
                info[str(i)] = content[i]
            content = info
        else:
            content = info

        archivo.close()
        
        return content
    
    def ReadJSON(self):
        with open(self.name,'r') as file:
            data = json.load(file)
        file.close()
        for key in data:
            if key != 'fs':
                data[key] = array(data[key])
        return data
        
    
    def WriteWav(self):
        for key in self.data:
            if key != 'fs':
                break
        amplitude = iinfo(int16).max
        m = max(self.data[key])
        p = int(amplitude/m)
        data = p*self.data[key]
        wavfile.write(self.name,int(self.data['fs']), data.astype(int16))
        
    def WriteMat(self):
        savemat(self.name, self.data)
    
    def WriteTxt(self):
        '''el numero de filas debe ser igual que el de columnas'''
        key = list(self.data.keys())[0]
        t = Signal().getTime_axis(len(self.data[key]),0,self.data['fs'])
        lines = []
        with open(self.name,'w') as file:
            
            for key in self.data:
                if key != 'fs':
                    file.write('{},'.format(key))
                    lines.append(self.data[key])
            lines.append(t)
            file.write('t\n')
            lines = transpose(array(lines))
            for line in lines:
                line = list(line)
                line = str(line).replace('[', '')
                line = line.replace(']', '\n')
                file.write(line)
            
        file.close()
    
    def WriteJSON(self):
        with open(self.name,'w') as file:
            Json = {'fs' : self.data['fs']}
            for key in self.data:
                if key != 'fs':
                    try:
                        Json[key] = list(self.data[key])
                    except Exception:
                        Json[key] = self.data[key]
            file.write(json.dumps(Json))
    

class Signal:
    
    def getSignal(self,route):
        return SignalFile(route, 'r').Gen()
    
    def getTime_axis(self,n , i = 0, fs = 1):
        return linspace(0, (n-1)/fs, n)
    
    def setSignal(self, filename, data):
        '''data es un diccionario'''
        d = data
        SignalFile(filename,'w',d).Gen()
        
    def getSpec(self,fs,data):
        X = fft(data)
        n = len(data)
        f = linspace(0,n-1,n)*fs/n
        return f, X
    
    def Decimate(self,data ,fs ,newfs, Aaliasing = True):
        'Against aliasing'
        if Aaliasing:
            fp = newfs/2
            digit = len(str(int(fp)))
            tr_band = 5*10**(digit-2)
            fc, ChebFltr = Filter.Chebyshev(.5, 60, fp + tr_band, fp + 2*tr_band)
            ChebFltr = Filter.BilinearTF(fs, ChebFltr)
            D = self.FilterSignal(data, ChebFltr)
            
        else:
            D = data
        re_m = int(round(fs/newfs))
        D = D[::re_m]
        return D
        
    
    def Interpole(self,fs ,data ,newfs , inter = 'Univariate Spline'):
        opcion = {
            'pchip': PchipInterpolator,
            'Akima': Akima1DInterpolator,
            'Spline': CubicSpline,
            'Univariate Spline' : InterpolatedUnivariateSpline
           }
        inter = opcion[inter]
        x = self.getTime_axis(len(data),fs = fs)
        f = inter(x,data)
        l_new = int(newfs/fs)*len(data)
        x_new = self.getTime_axis(l_new, fs = newfs)
        data_new = f(x_new)
        return data_new
    
    def FilterSignal(self,data, Filtro, IIR = True):
        if IIR:
            Filtro.reverse()
            for num,den in Filtro:
                data = lfilter(num, den, data)
            return data
        
        elif not IIR:
            data = lfilter(Filtro, [1], data)
            
    def Cut(self, data, fs, ti, tf):
        corte_ti = int(ti*fs + 1)
        corte_tf = int(tf*fs + 1)
        new_data = data[corte_ti : corte_tf]
        return new_data
    
    def Create(self, dictionary, data, keys):
        for key in keys:
            dictionary[key] = data[key]
        return dictionary
    
            