t=int(input())

for i in range(t):
    temp=[str(bin(int(x)))[2:] for x in input().split()]   
    long=max(len(temp[0]),len(temp[1]))
    dis=max(len(temp[0]),len(temp[1]))-min(len(temp[0]),len(temp[1]))
    if(len(temp[0])>len(temp[1])):
        for k in range(dis):
            temp[1]='0'+temp[1]
    else:
        for k in range(dis):
            temp[0]='0'+temp[0]
    for j in range(long-1,-1,-1):
        if(temp[0][j]!=temp[1][j]):
                print(long-j)
                break