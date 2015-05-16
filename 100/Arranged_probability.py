import sys
import math

N=int(sys.argv[1])

a=0
b=1

i=0
while i<N:
    c=a
    a=b
    b=2*a+c
    
    if (1+math.sqrt(2*b**2-1))/2>1000000000000:
        print((b+1)/2)
    
    i+=1
    