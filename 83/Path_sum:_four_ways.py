import sys

data=open(sys.argv[1], "r")

matrix=[i.split(',') for i in data]
matrix = [[[0,int(j),0] for j in i] for i in matrix]

data.close()

N=len(matrix[0])
M=0
for i in range(0,N):
    for j in range(0,N):
        M=M+matrix[i][j][1]

for i in range(0,N):
    for j in range(0,N):
        matrix[i][j][2]=M+1

matrix[0][0][2]=matrix[0][0][1]

numberunsettled=N**2

while numberunsettled>0:
    a=-1
    b=-1
    m=M+1
    for i in range(0,N):
        for j in range(0,N):
            if matrix[i][j][0]==0 and matrix[i][j][2]<m:
                m=matrix[i][j][2]
                a=i
                b=j
    
    matrix[a][b][0]=1
    
    if a-1>-1:
        matrix[a-1][b][2]=min(matrix[a-1][b][2], matrix[a][b][2]+matrix[a-1][b][1])
    if b-1>-1:
        matrix[a][b-1][2]=min(matrix[a][b-1][2], matrix[a][b][2]+matrix[a][b-1][1])
    if a+1<N:
        matrix[a+1][b][2]=min(matrix[a+1][b][2], matrix[a][b][2]+matrix[a+1][b][1])
    if b+1<N:
        matrix[a][b+1][2]=min(matrix[a][b+1][2], matrix[a][b][2]+matrix[a][b+1][1])
    
    numberunsettled=numberunsettled-1

print(matrix[N-1][N-1][2])


#131,673,234,103,18
#201,96,342,965,150
#630,803,746,422,111
#537,699,497,121,956
#805,732,524,37,331

#2297