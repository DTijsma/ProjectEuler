import sys
import math

#Example input: python3 3/Multiples_of_3_and_5.py 100

N=int(sys.argv[1])

lijst=[]

for i in range(N):
    lijst.append(1)


for k in range(1,int(N/3)+1):
    lijst[3*k-1]=0

for k in range(1,int(N/5)+1):
    lijst[5*k-1]=0


som=0
for k in range(1,N):
    if lijst[k]==0:
        som=som+(k+1)
        
print('The sum of all multiples of 3 and 5 below', N, ' is equal to', som)