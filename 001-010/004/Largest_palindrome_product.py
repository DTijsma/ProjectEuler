import sys

#Example input: python3 3/Largest_palindrome_product.py 999 prime.dat 

N=int(sys.argv[1])

lijst=[]
lijst2=[]
lijst3=[]

for i in range(100,N+1):
    lijst.append(i)

for j in lijst:
    for k in range(j-100,N-99):
        lijst2.append(str(j*lijst[k]))

for m in lijst2:
    if m[0]==m[-1] and m[1]==m[-2] and m[2]==m[-3]:
        lijst3.append(int(m))

print(max(lijst3))
    