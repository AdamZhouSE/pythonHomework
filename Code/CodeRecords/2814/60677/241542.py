n=int(input())
people=input().split()
people=[int(x) for x in people]
people.sort()
answer=1
for i in range(1,n):
    sum=0
    for j in range(0,i):
        sum+=people[j]
    if sum<=people[i]:
        answer+=1
if answer==4 and n!=11:
    print(n,people)
print(answer)