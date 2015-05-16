import sys

N=int(sys.argv[1])

startingnumber=0
maxlength=0

def function(n):
    length=0
    while n>1:
        if n%2==0:
            n=int(n/2)
            length=length+1
        else:
            n=3*n+1
            length=length+1
    
    return length+1


for n in range(1,N):
    if function(n)>maxlength:
        startingnumber=n
        maxlength=function(n)

print(startingnumber)