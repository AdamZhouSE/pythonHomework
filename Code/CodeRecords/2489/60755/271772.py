string = input()
l = string[1:-1].split(",")
for i in range(len(l)):
    l[i] = int(l[i])
lower = int(input())
upper = int(input())
res = 0
for i in range(1,len(l)):
    for k in range(len(l)-i+1):
        if lower<=sum(l[i:i+k])<=upper:
            res = res +1
print(res)