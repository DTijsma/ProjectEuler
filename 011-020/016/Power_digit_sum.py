import math

number=1
for i in range(100):
    number=number*(i+1)

getal=str(number)

som=0
length=math.ceil(math.log(number)/math.log(10))

for i in range(0,length):
    som=som+int(getal[i])
    
print(som)