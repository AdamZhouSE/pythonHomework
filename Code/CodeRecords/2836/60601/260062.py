n = eval(input())
num = list(map(int,input().split(' ')))
target = sorted(num)
old = list(num)
if target == old:
    print(0)
    exit(0)
tail = num[-1]
num = num[0:-1]
num.insert(0,tail)
count = 1
while num != old and num!= target:
    tail = num[-1]
    num = num[0:-1]
    num.insert(0, tail)
    count = count + 1
if num == target:
    print(count)
else:
    print(-1)