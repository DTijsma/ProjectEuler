import sys

N=int(sys.argv[1])

som1=0
som2=0

for i in range(N+1):
    som1=som1+i**2

for j in range(N+1):
    som2=som2+j

som2kwadraat=som2**2

print(som1)
print(som2kwadraat)
print(som2kwadraat-som1)
