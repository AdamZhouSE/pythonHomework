mx=0
n=int(input())
people=[]
for i in range(n):
    person=input().split(' ')
    person=list(map(int,person))
    people.append(person)
for i in range(n):
    temp=people[:]
    temp.pop(i)
    time=[False]*100000
    for p in temp:
        for t in range(p[0],p[1]):
            time[t]=True
    res=0
    for j in time:
        if j:
            res+=1
    if res>mx:
        mx=res
print(mx,end='')