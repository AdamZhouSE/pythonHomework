a = int(input())
for i in range(a):
    b,c= map(int,input().split())
    d = list(map(int,input().split()))
    e = list(map(int,input().split()))
    sign = True
    for j in e:
        if j not in d:
            sign = False
            break
    if sign :
        print("Yes")
    else:
        print("No")
