import numpy as np
import sys
import math


print "Marcha Aleatoria corriendo..............."

nM=int(sys.argv[1]) # numero de Marchas 

promedio=[] # lista  que  guarda el promedio
promi=0
i=0
j=0

numpasos=0



piconst=math.pi

for i in range (50):

    hastan=(10*(i+1))
    cont=0

    for j in range (nM): #hasta nM marchas 
        x=0 
        y=0
        z=0
        xp=0
        yp=0
        zp=0
        r=0
        numpasos=0 # numero de  pasos  hastan 

        while r<=hastan:
            phi =np.random.rand()*piconst
            theta=np.random.rand()*piconst*2
            
            xp= np.sin(phi)* np.cos(theta) #paso en x 
            yp= np.sin(phi)* np.sin(theta) #paso en y
            zp= np.cos(phi) #paso en z 
    
            x=x+xp
            y=y+yp
            z=z+zp

            numpasos=(numpasos + 1)
            #print "numero paso", numpasos
            #r=(x**2+y**2+z**2)**0.5 # 5minutos 
            r=(r**2+2*(x*xp+y*yp+z*zp)+1)**0.5 # 2 minutos un poco menos 
            #print r

        print "hasta", hastan, "numero pasoso", numpasos

        cont= cont + numpasos
        #print "cont", cont

        #print "despues" 

    #print "final segundo for", hastan
    promi = cont/nM
    promedio.append(promi)

print "fuera del primer for", promedio

#nombre[50]=""

outfile=open("nombre.dat", "w")
for k in range(50):
 
    hasta=str(10*(k+1))+" "
    promedink=str(promedio[k])+" "

    aline= outfile.write(hasta +  promedink + "\n")
outfile.close()
    

