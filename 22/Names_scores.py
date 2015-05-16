import sys

invoer=[]

data=open(sys.argv[1], "r")
for line in data:
    invoer.append(line)

data.close()

invoer[0]=invoer[0].replace('"', ' ')
invoer[0]=invoer[0].split(',')

invoer[0]=sorted(invoer[0])
print(invoer[0][937])


som=0
for i in range(len(invoer[0])):
    getal=0
    for j in range(len(list(invoer[0][i]))):
        getal=getal+ord(list(invoer[0][i])[j])-64
    getal=getal+64
    som=som+(i+1)*getal

print(som)