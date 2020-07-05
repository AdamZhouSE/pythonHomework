def grayCode():
    gray=int(input())
    gray=bin(gray)[2:]
    natureBin=""+gray[0]
    res=0
    for i in range(1,len(gray)):
        natureBin+=str(int(gray[i])^int(natureBin[i-1]))
    for i in range(0,len(natureBin)):
        if natureBin[len(natureBin)-1-i]=='1':
            res+=2**i
    print(res)

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        grayCode()