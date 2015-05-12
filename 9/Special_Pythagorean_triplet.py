
lijstje=list(range(1,126))

lijstje2=[]

for m in lijstje:
    for n in lijstje:
        if 2*m**2+2*m*n==1000:
            lijstje2.append((m,n))
            

print(lijstje2)