n = int(input())
for i in range(n):
    a,b = input().split()
    if int(a) >= int(b)*(int(b)+1)/2:
        print("1")
    else:
        print("0")