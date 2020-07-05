t = int(input())

for i in range(t):
    a,b = input().split()
    a = int(a)
    b = int(b)
    sum=(b*(b+1))//2
    if sum<=a:
        print("1")
    else:
        print("0")