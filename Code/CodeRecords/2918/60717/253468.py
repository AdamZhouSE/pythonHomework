n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
count=0
while len(list1)!=0:
    maxx=max(list1)
    list1.remove(maxx)
    tmp=[]
    while maxx in list1:
        tmp.append(maxx)
        list1.remove(maxx)
    while maxx!=0 and len(list1)>0:
        nextt=max(list1)
        maxx=min(maxx-1,nextt)
        list1.remove(nextt)
        while nextt in list1:
            tmp.append(nextt)
            list1.remove(nextt)
    count+=1
    for i in tmp:
        list1.append(i)
print(count)