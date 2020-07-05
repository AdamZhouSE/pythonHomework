n=int(input())
src=[int(x) for x in input().split()]
ans=[]
def reverse_in_array(start,end):
    tmp=[]
    for i in range(start,end):
        tmp.append(src[i])
    tmp=list(reversed(tmp))
    curr=0
    for i in range(start,end):
        src[i]=tmp[curr]
        curr+=1
for i in range(n):
    minindex=i
    minvalue=src[i]
    for j in range(i+1,n):
        if src[j]<minvalue:
            minvalue=src[j]
            minindex=j
    if minindex!=i:
        reverse_in_array(i,minindex+1)
    ans.append(minindex+1)
print(*ans,end=' ')
        