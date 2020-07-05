str1=input()
set1=set()
for i in range(1,len(str1)+1):
    for j in range(0,len(str1)-i+1):
        set1.add(str1[j:(j+i)])
ans=0
for temp in set1:
    a=temp[0]
    set2=set(a)
    change=0
    for j in range(0,len(temp)-1):
        if temp[j]!=temp[j+1]:
            change+=1
    if change<2:
        ans+=1
print(ans)