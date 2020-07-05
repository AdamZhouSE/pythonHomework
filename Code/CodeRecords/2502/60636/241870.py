number=int(input())
lists=[]
for i in range(number):
    lists.append(int(input()))
ans=0
for i in range(1,number):
    ans=ans+max(lists[i],lists[i-1])
print(ans)