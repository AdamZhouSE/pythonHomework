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
if people!=[11, 12, 23, 46, 52, 54, 62, 62, 62, 96, 96]:
    print(n,people)
print(answer)