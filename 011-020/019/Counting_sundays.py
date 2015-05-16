normalyear=[3,3,0,3,2,3,2,3,3,2,3,2]
leapyear=[3,3,1,3,2,3,2,3,3,2,3,2]

lijst=[4]
for i in range(1,101):
    if i%4==0:
        for m in range(12):
            lijst.append((lijst[-1]+leapyear[m])%7)
    else:
        for n in range(12):
            lijst.append((lijst[-1]+normalyear[n])%7)

#for k in range(len(normalyear)):
#            lijst.append((lijst[-1]+normalyear[k])%7)

print(lijst.count(4)-1)