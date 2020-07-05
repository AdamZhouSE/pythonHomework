
T=int(input())
for t in range(0,T):
    length=int(input())
    matrix=[[0]*length for _ in range(length)]
    string=[int(k) for k in input().split()]
    res=''
    for i in range(0,length):
        for j in range(0,length):
            matrix[i][j]=string[i*length+j]
            res+=' '
            res+=str(matrix[i][j])
    
    for i in range(0,length):
        for j in range(i,length):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
    for i in range(0,length):
        for j in range(0,length//2):
            matrix[i][j],matrix[i][length-1-j]=matrix[i][length-1-j],matrix[i][j]
    
    res=''
    for i in range(0,length):
        for j in range(0,length):
            res+=' '
            res +=str(matrix[i][j])
    print(res[1:])

        