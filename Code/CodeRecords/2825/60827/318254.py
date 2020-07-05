
n = int(input())
l = []
t=0
for i in range(n):
    temp = sum([int(x) for x in input().split()])
    if i==0:
        t=temp
    l.append(temp)
l.sort(reverse=True)
print(l.index(t)+1)
