a=int(input())
for k in range(0,a):
    a=input()
    b = input().split(' ')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    a=int(input())
    b.sort()
    print(b[a-1])