n=int(input())
before=[]
after=[]
for i in range(n):
    area=input().split()
    before.append(int(area[0]))
    after.append(int(area[1]))
filterBefore=[]
filterAfter=[]

for i in range(n):
    if before[i] not in filterBefore:
        max=after[i]
        for k in range(n):
            if max<after[k] and before[i]==before[k]:
                max=after[k]
        filterAfter.append(max)
        filterBefore.append(before[i])

dictionary = dict(zip(filterBefore, filterAfter))

dictionary=sorted(dictionary.items(),key=lambda x:x[0])

head=[]
tail=[]
start=dictionary[0][0]
end=dictionary[0][1]
head.append(start)
for i in range(1,len(dictionary)):
    if dictionary[i][0]>end:
        start=dictionary[i][0]
        tail.append(end)
        end=dictionary[i][1]
        head.append(start)

    else:
        end=dictionary[i][1]
tail.append(end)
for i in range(len(head)):
    print(str(head[i])+' '+str(tail[i]))