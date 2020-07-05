nm=input().split(' ')
n=int(nm[0]);m=int(nm[1])
people=[0]*n
for i in range(m):
    temp=[0]*n
    votes=input().split(' ');votes=[int(x) for x in votes]
    for j in range(n):
        temp[j]+=votes[j]
    winnner=temp.index(max(temp))
    people[winnner]+=1
print(people.index(max(people))+1)