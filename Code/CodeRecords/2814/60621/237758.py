a=int(input())
b=[int(t) for t in input().split()]
count=0
b.sort()
num=0
for i in b:
    if i>=count:
        count+=i
        num+=1
print(num)