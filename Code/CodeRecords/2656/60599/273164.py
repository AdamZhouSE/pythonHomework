def two(k):
    res=""
    while(k>1):
        if(k%2!=0):
            res="1"+res
        else:
            res="0"+res
        k=k//2
    res="1"+res
    return res

u=int(input())
for z in range(u):
    s=list(map(int,input().split(' ')))
    k1=two(s[0])
    k2=two(s[1])
    while len(k1)<len(k2):
        k1="0"+k1
    while len(k1)>len(k2):
        k2="0"+k2
    for i in range(len(k1)-1,0,-1):
        if(k1[i]!=k2[i]):
            print(len(k1)-i)
            break