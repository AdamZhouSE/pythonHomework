n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
count=0
while len(list1)!=0:
    maxx=max(list1)
    list1.remove(maxx)
    while maxx!=0 and len(list1)>0:
        nextt=max(list1)
        maxx=min(maxx-1,nextt)
        list1.remove(nextt)
    count+=1
print(count)