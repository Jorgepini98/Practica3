# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import time
import csv
import matplotlib
# matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np

arduino = serial.Serial('COM4', baudrate = 115200, timeout = 1.0)

time1 = 0;

x = np.array([0])
y = np.array([0])
z = np.array([0])

data = ""

inputLine = '0.07,0.5,1.5'

fig, ax = plt.subplots()




while True:
    
     try:
         
         
        if (arduino.inWaiting() > 0):
    
        
            try:
                    
                line = str(inputLine) #str(arduino.readline())
                
            except:
                    
                continue
        
            # with open("test_data.csv","a") as f:
                
            #     writer = csv.writer(f,delimiter=",")
            #     writer.writerow([line])
                    
                
            data =  line.split(',')
            
            x = np.append([x],[float(data[0])])
            y = np.append([y],[float(data[1])])
            z = np.append([z],[float(data[2])])
            
           
                        
                    
            if(time.time() - time1 > 5):
                
                xMedia = np.mean(x)
                yMedia = np.mean(y)
                zMedia = np.mean(z)
                
                print("X MEAN :", xMedia)
                
                xDes = np.std(x)
                yDes = np.std(y)
                zDes = np.std(z)
                
                print("X STD :", xDes)
                
                
                ax.plot(tiempo, media, color = 'tab:purple')
                ax.plot(tiempo, varianza, color = 'tab:green')
                plt.show()
                    
                    
                x = np.array([0])
                y = np.array([0])
                z = np.array([0])
                    
                time1 = time.time()
                
                
                   
   
           
     except:
         arduino.close()
         print("Keyboard Interrupt")
         break
        
        

