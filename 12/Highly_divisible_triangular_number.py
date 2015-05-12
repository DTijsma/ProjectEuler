import sys
import math

lijst=[]
lijstje=[]

N=int(sys.argv[1])
data=open(sys.argv[2], "r")

primelist=[]
for line in data:
    primelist.append(int(line.replace('\n', '')))

data.close()

for i in range(N):
    lijst.append(i+sum(lijstje))
    lijstje.append(i)

primefactors=[]

lijst2=[]

for getal in lijst:
    getal2=getal
    delers=1
    for item in primelist:
        if getal>1:
            if getal%item==0:
                k=0
                while getal%item==0:
                    k=k+1
                    getal=int(getal/int(item))
                delers=delers*(k+1)
        elif getal==1:
            getal=0
    if delers>500:
        lijst2.append(getal2)

if len(lijst2)>0:
    print(lijst2[0])
else: 
    print('Deze N is niet voldoende.')


#print(lijst)


for i in range(N):
    lijst.append(i+sum(lijstje))
    lijstje.append(i)