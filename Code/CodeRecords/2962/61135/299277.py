inp=input().split(" ")
N=int(inp[0])
P=int(inp[1])
strlis=input().split(" ")
numlis=list()
res=list()
for a in range(0,N):
    mid=(ord(strlis[a][-1])-ord('A'))+32*(ord(strlis[a][-2])-ord('A'))+1024*(ord(strlis[a][-3])-ord('A'))
    numlis.append(mid)
    ind=mid%P
    count=0
    temp=0
    sig=0
    temp=ind
    while(True):
        if ind not in res:
            res.append(ind)
            count=0
            break
        else:
            count=count+1
            if(sig==0):
                ind=(temp+count*count)%P
                sig=sig+1
            else:
                count=count-1
                sig=0
                ind=(temp-count*count)%P
for b in range(0,N-1):
    print(str(res[b])+" ",end="")
print(res[N-1])