s=input().split(" ")
N,P=int(s[0]),int(s[1])
s=input().split(" ")
result=[]
for i in range(N):
    string=s[i]
    res=((ord(string[-3])-ord("A"))*32*32+(ord(string[-2])-ord("A"))*32+(ord(string[-1])-ord("A")))%P
    j=1
    index=res
    while index in result:
        index=(res+j*j)%P
        if index in result:
            index=(res-j*j)%P
        j+=1
    result.append(index)
print(" ".join(str(i) for i in result))