import os
import linecache
import numpy
import math
import itertools #遍历循环模块
#qinzhen 2021.10.25
def stepOf_CONTCAR():#获取CONTCAR数量
    a=[c for a,b,c in os.walk(os.getcwd())][0]
    a=[a for a in a if "CONTCAR_" in a]
    return len(a)-1

def bond_length(CONTCARnumber,atom1,atom2):  #获取键长的模块
    def zhouqixing(ap1,ap2):
        d=numpy.zeros((1,3))
        for i in range (0,3):
                    d[:,i]=ap1[i]-ap2[i]
                    if abs(d[:,i]) <= 0.5:
                            d[:,i]=d[:,i]
                    else:
                            if ap1[i]>ap2[i]:
                                    d[:,i]=ap1[i]-ap2[i]-1
                            else:
                                    d[:,i]=ap1[i]-ap2[i]+1
        return d
    
    a1=atom1
    a2=atom2
    a=zuobiao(CONTCARnumber,3)
    b=zuobiao(CONTCARnumber,4)
    c=zuobiao(CONTCARnumber,5)
    axis=numpy.array((a,b,c))
    atom1=zuobiao(CONTCARnumber,int(atom1)+8);
    atom2=zuobiao(CONTCARnumber,int(atom2)+8);

    d=zhouqixing(atom1,atom2)
   
    d=numpy.dot(d,axis)
    
    bl=math.sqrt((d[:,0]**2)+(d[:,1]**2)+(d[:,2]**2))
    return bl
def zuobiao(CONTCARnumber,rownumber):
        a=numpy.array([float(a) for a in linecache.getline('CONTCAR_{}'.format(CONTCARnumber),rownumber).split()],dtype=numpy.float64)
        return a
def getZuHe(min_length,max_length):      #获取指定键长范围内 元素序号(type:字典)
        ZuHe=list(itertools.combinations(range(1,NumberOfAtoms+1), 2))
        a=dict()
        for i in ZuHe:
            bl=bond_length(0,i[0],i[1])
            if   min_length<=bl<=max_length:
                a.update({i:bl})
        return a

#主要
def mains(min_length,max_length,outfile="length.dat"):
    
    step=stepOf_CONTCAR()
    global NumberOfAtoms
    NumberOfAtoms=int(zuobiao(0,7).sum())
    
    a = (getZuHe(min_length,max_length))
    f=open(outfile,"w+")
    for i in a:
            print('{}_{}'.format(i[0],i[1]).ljust(13),end=" ",file=f)
            if i is list(a.keys())[-1]:
                print(" ",file=f)
    for n in range(0,step+1): 
        for i in a:
            print( "%5f".ljust(4)%(bond_length(n,i[0],i[1])),end=" ",file=f)
        print(" ",file=f)

    f.close()
#mains(min_length=(float(input("min_length:"))),max_length=(float(input("max_length:"))
mains(min_length=1.4,max_length=1.9,outfile="强.dat")
mains(min_length=1.9,max_length=2.0,outfile="弱.dat")

