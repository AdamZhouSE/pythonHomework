n = int(input())
li = []
target=0
for i in range(n):
    temp = sum([int(x) for x in input().split()])
    if i==0:
        target=temp
    li.append(temp)
li.sort(reverse=True)
print(li.index(target)+1)