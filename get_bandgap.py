# -*- coding:utf-8 -*-
from sys import exit
from os.path import exists
from os import popen
from os import remove
#This edition is updated on 2020.4.11 by qinzhen, 1772389715@qq.com   
#If the DOSCAR have been exists?
if exists("DOSCAR"):
    pass
else:
    print("ERROR! The file DOSCAR  don't exist. ")
    exit()
#How much rows of  Total DOS?  (at DOSCAR 6 rows, 3  columns )
E_fermi = float(popen(" grep E-fermi OUTCAR|tail -1 |awk '{printf $3}' ").read())

#python2.7
print(E_fermi)
#python3
#print(f"E_fermi: { E_fermi } ")

#Get data of DOSCAR
DOSCAR_file = open("DOSCAR", "r")
DOSCAR_data = DOSCAR_file.readlines()
DOSCAR_file.close()
TotalDOS_end = int(DOSCAR_data[5].strip('\n').split()[2])

#Total dos
Tdos_file = open("Tdos.dat","w")
bandgap_file = open("bandgap.dat","w")
Record_Integral=0
Record_Energy=-1000
for rows in range(7,TotalDOS_end +1 ):
    print(DOSCAR_data[rows].strip('\n'))
#define valuate
    Energy = float(DOSCAR_data[rows].split()[0]) - E_fermi
    dos = float(DOSCAR_data[rows].split()[1])
    Integral = float(DOSCAR_data[rows].split()[2])
    
#write Tdos
    if abs(Energy) < 0.02:
        file = open('E_fermi_dos.dat','a+')
        file.write(str(Energy)+'  '+ str(dos) +'\n')
    Tdos_file.write(str(Energy)+'  '+ str(dos) +'\n')
#write bandgap
    if abs(dos)<0.001  :
        if Integral != Record_Integral and abs(Energy)<abs(Record_Energy):
            bandgap_file.seek(0)          
            bandgap_file.truncate()
            Record_Integral = Integral
            Record_Energy = Energy
        if float(DOSCAR_data[rows-1].split()[1])>0.001:
                k =  ( float(DOSCAR_data[rows-1].split()[1]) - float(DOSCAR_data[rows-2].split()[1]) )/(float(DOSCAR_data[rows-1].split()[0]) - float(DOSCAR_data[rows-2].split()[0]) )
                PS = float(DOSCAR_data[rows-1].split()[1])/k
                if k < 0 and abs(PS) < abs((float(DOSCAR_data[rows].split()[0]) - float(DOSCAR_data[rows-1].split()[0]))):
                    d = float(DOSCAR_data[rows-1].split()[0])+abs(PS) - E_fermi
                    bandgap_file.write(str( round(d,4) )+'    '+'0.0'+'\n')
           
        if Integral == Record_Integral:
            if abs(Energy)<abs(Record_Energy):
                Record_Energy = Energy
            bandgap_file.write(str(Energy)+'    '+ str(dos) +'    '+str(Integral) +'\n')  
            if float(DOSCAR_data[rows+1].split()[1])>0.001:
                k =  ( float(DOSCAR_data[rows+2].split()[1]) - float(DOSCAR_data[rows+1].split()[1]) )/(float(DOSCAR_data[rows+2].split()[0]) - float(DOSCAR_data[rows+1].split()[0]) )
                PS = float(DOSCAR_data[rows+1].split()[1])/k  
                if k > 0 and abs(PS) < abs((float(DOSCAR_data[rows+1].split()[0]) - float(DOSCAR_data[rows].split()[0]))):
                    d = float(DOSCAR_data[rows+1].split()[0]) - abs(PS) - E_fermi
                    bandgap_file.write(str( round(d,4) )+'    '+'0.0'+'\n')
    
       
bandgap_file.close()
#band gap
bandgap_file = open("bandgap.dat","r+")
data=bandgap_file.readlines()
Calculated_value=abs(float(data[0].split()[0]) - float(data[-1].split()[0]))  
bandgap_file.write( str(Calculated_value)  )

