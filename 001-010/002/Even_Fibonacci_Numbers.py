import sys

#Example input: python3 1/Even_Fibonacci_Numbers.py 33

N=int(sys.argv[1])

a=0
b=1
EvenFibonacciSum=0

for i in range(N):
    c=a
    a=b
    b=b+c
    
    if i%3==1 and b<4000000:
        EvenFibonacciSum=EvenFibonacciSum+b
    
    i=+1

print('The sequence Fn is defined by F1=1, F2=1 and F(n+2)=F(n+1)+Fn for n greater or equal to 1.')
print('F'+ str(N-1) + ' =', a)
print('F'+ str(N) + ' =', b)
print('Sum of the even Fibonacci numbers (Fn%2==0) with Fn\le 4000000 is equal to:')
print(EvenFibonacciSum)
