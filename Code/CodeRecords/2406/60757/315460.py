n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))
maxins=0
aind=0
bind=0
for i in range(n):
    for j in range(i+1,n):
        if li[j]<li[i]:
            if j-i>maxins:
                maxins=j-i
                aind=i
                bind=j
tmp=li[aind]
li[aind]=li[bind]
li[bind]=tmp
count=0
for i in range(n-1):
    for j in range(n-1-i):
        if li[j]>li[j+1]:
            tmp=li[j]
            li[j]=li[j+1]
            li[j+1]=tmp
            count+=1
print(count)
