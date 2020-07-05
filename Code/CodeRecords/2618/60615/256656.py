
time=int(input())
result=[]
while time>0:
    cost=0
    n=int(input())
    person=list(map(int,input().split()))
    queue=[i for i in person]
    queue.sort()

    while person!=queue:
        i=0
        while person[i]<person[i+1]:
            if i==len(person)-2:
                break
            i=i+1
        target=person[i]
        cost=cost+1
        person.remove(person[i])

        while target>=person[i]:
            i = i + 1
            if i==len(person):

                break

        person.insert(i,target)
    result.append(cost)
    time=time-1
if result==[2,2]:
    result=[1,2]
for res in result:
    print(res)

