import sys

invoer=[]

data=open(sys.argv[1], "r")
for line in data:
    invoer.append(int(line.replace('\n', '')))

data.close()


print(sum(invoer))