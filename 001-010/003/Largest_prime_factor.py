import sys
import math

N=int(sys.argv[1])
data=open(sys.argv[2], "r")

primelist=[]
for line in data:
    primelist.append(int(line.replace('\n', '')))

data.close()

primefactors=[]

for item in primelist:
    if N>1:
        if N%item==0:
            primefactors.append(item)
            while N%item==0:
                N=int(N/int(item))
    elif N==1:
        N=0

print(primefactors)
print(N)
print('Largest primefactor =', primefactors[len(primefactors)-1])
