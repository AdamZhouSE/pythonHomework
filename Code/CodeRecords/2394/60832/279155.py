All = int(input())

for q in range(0, All):
    length = int(input())
    temp = list(map(int, input().split()))
    num=0

    ar=[]
    for x in temp:
        if x==0:
            num+=1
        else:
            ar.append(x)
    for i in range(num):
        ar.append(0)

    ans = ''

    for x in ar:
        ans += str(x) + ' '
    print(ans)