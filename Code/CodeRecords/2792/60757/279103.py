n=int(input())
li=list(map(int,input().split()))
re1=li.count(1)
re2=[]

for i in range(1,len(li)):
    if li[i]==1:
        re2.append(li[i-1])
re2.append(li[len(li)-1])
print(re1)
for i in range(re1-1):
    print(re2[i],end=' ')
print(re2[re1-1])
    