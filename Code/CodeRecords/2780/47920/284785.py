t = int(input())
for i in range(t):
    n = int(input())
    li = input().split(' ')
    k = int(input())
    cheng = 1
    for i in range(n):
        cheng = cheng *int(i)
print(cheng % k)