# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

 #importo las librerias
 
import serial
import time
import csv
import matplotlib
import re
import matplotlib.pyplot as plt
import numpy as np

#defino el objeto serial
arduino = serial.Serial('COM3', baudrate = 115200, timeout = 1.0)

time1 = 0;

#inicializo variables
x = np.array([0])
y = np.array([0])
z = np.array([0])

data = ""



while True:
    
     try:
         
         #si tiene para leer en el buffer
        if (arduino.inWaiting() > 0):
    
        
            try:
                    #lee una linea del buffer
                line = arduino.readline()
                #pasamos los datos a float
                line = line.decode('utf-8') #convert byte to str
                data = [float(s) for s in re.findall(r'-?\d+\.?\d*', line)]
                
            except:
                    
                continue
            
            #guardar datos en .cvs
        
            # with open("test_data.csv","a") as f:
                
            #     writer = csv.writer(f,delimiter=",")
            #     writer.writerow([line])
                    
                
            
            #almacenamos datos en arryas
            x = np.append([x],[round(data[0],2)])
            y = np.append([y],[round(data[1],2)])
            z = np.append([z],[round(data[2],2)])
            
           
                        #cuando han pasado 5 sec calculamos media y varianza y plotemos datos de entrada 
                    
            if(time.time() - time1 > 5):
                
                xMedia = np.mean(x)
                yMedia = np.mean(y)
                zMedia = np.mean(z)
                
                print("X MEAN :", xMedia)
                
                xDes = np.std(x)
                yDes = np.std(y)
                zDes = np.std(z)
                
                print("X STD :", xDes)
                
                plt.subplot(1,3,1)
                
                plt.plot(x, color = 'tab:red')
                
                plt.subplot(1,3,2)
                
                plt.plot(y, color = 'tab:green')
                
                plt.subplot(1,3,3)
                
                plt.plot(z, color = 'tab:blue')
                
                plt.show()
                    
                    
                x = np.array([0])
                y = np.array([0])
                z = np.array([0])
                
                
                    
                time1 = time.time()
                
                
                   
   
           
     except:
         arduino.close()
         break
         
        
        

