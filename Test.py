
lijst=[]
for m in range(1,23):
    for n in range(1,m):
        for k in range (1,201):
            if 2*m*(m+n)*k<1000:
                lijst.append(2*m*(m+n)*k)
            if 2*m*(m+n)*k==960:
                print((k*(m**2-n**2),2*m*n*k,k*(m**2+n**2)))

#getal=0
#aantal=0
#for t in range(1,1001):
#    if lijst.count(t)>aantal:
#        getal=t
#        aantal=lijst.count(t)

#print(getal)
#print(aantal)
#print(lijst.count(120))