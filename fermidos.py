from os.path import exists
from os import popen
from os import remove
#open('{0}.txt'.format(j),'a+')
fermi= open('fermi','a+')
doss= open('doss','a+')
for j in range(1,8):
    DOSCAR_file = open("DOSCAR_{0}".format(j), "r")
    DOSCAR_data = DOSCAR_file.readlines()
    DOSCAR_file.close()
    TotalDOS_end = int(DOSCAR_data[5].strip('\n').split()[2])
    E_fermi=float(DOSCAR_data[5].strip('\n').split()[3])
    num=0
    for rows in range(8,TotalDOS_end +1 ):
#    print(DOSCAR_data[rows].strip('\n'))
#define valuate
        Energy = float(DOSCAR_data[rows].split()[0]) - E_fermi
        dos = float(DOSCAR_data[rows].split()[1])
        Integral = float(DOSCAR_data[rows].split()[2])
         
        if Energy > 0:
#            file = open('Edos_{j}.dat'.format(j),'a+')
#            file.write(str(Energy)+'  '+ str(dos) +'  '+ str(Integral)+'\n')
#        if abs(Energy) == 0:
#            E=rows
            num+=1
            if num == 1:
                E=rows
#            doss.write(str(dos)+'\n')
#        if Energy > 0:
#            F=rows  
    totaldos=float(DOSCAR_data[E+1].split()[2])-float(DOSCAR_data[E-2].split()[2])
    file = open('Edos_{0}.dat'.format(j),'a+')
    file.write(str(totaldos)+'\n')
#    file.write(str(E_fermi))
    fermi.write(str(E_fermi)+'\n')
