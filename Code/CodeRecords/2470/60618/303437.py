T=int(input())
for t in range(0,T):
    length=int(input())
    matrix=[[0]*length]*length
    string=[int(k) for k in input().split()]
    for i in range(0,length):
        for j in range(0,length):
            matrix[i][j]=string[i*length+j]
    n = len(matrix)
    r = list(zip(*matrix[::-1]))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = r[i][j]
    re=''
    for i in range(0,length):
        for j in range(0,length):
            re=re+str(matrix[i][j])
            re=re+' '
            
    print(re)
            
        
        