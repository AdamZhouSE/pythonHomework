t = int(input())
for i in range(t):
    li = input().split()
    a = set(li[0])
    b = set(li[1])
    print(len(a|b))