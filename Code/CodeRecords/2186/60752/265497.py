lst=[1]
while len(lst)<1000:
    lst.append(lst[len(lst)-1]+len(lst)+1)

for i in range(int(input())):
    n=int(input())
    sum=0
    for j in range(n):
        sum+=lst[j]
    print(sum)