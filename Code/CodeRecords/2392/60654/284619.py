a = int(input())
for i in range(a):
    sign = False
    b,c = map(int,input().split())
    d = list(map(int,input().split()))
    for k in range(d.__len__()-1):
        for l in range(k+1,d.__len__()):
            if d[k]*d[l]==c:
                sign = True
    if sign:
        print("Yes")
    else:
        print("No")