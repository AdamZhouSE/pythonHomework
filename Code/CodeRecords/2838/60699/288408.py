input()
list1=list(map(int,input().split(' ')))
ans=0
start=0
end=len(list1)-1
list1.sort()
while start<end:
    ans+=(list1[start]+list1[end])*(list1[start]+list1[end])
    start+=1
    end-=1
print(ans)