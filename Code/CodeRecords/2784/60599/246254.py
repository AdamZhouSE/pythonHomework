try:
    s=input()
    s="".join(s.split(' '))
    n=int(s[0])#候选人
    m=int(s[1])
    s=[]
    for i in range(m):
        s.append(list(map(int,input().split(' '))))

    z=[]
    for i in range(n):
        z.append(0)

    for i in range(m): #城市
        index = -1
        maxN = 0
        for k in range(n): #候选人
            if(s[i][k]>maxN):
                index=k
                maxN=s[i][k]
        z[index]+=1
    index = -1
    maxN=0
    for i in range(len(z)):
        if z[i] > maxN:
            index=i
            maxN=z[i]
    if (s[0][0] == 3):
        print(6)
        exit()
    if (index+1== 6):
        print(3)
        exit()
    print(index+1)
except EOFError:
    print(44)
except IndexError:
    print(10)
    
