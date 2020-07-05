All = int(input())

for q in range(0, All):
    length = int(input())
    temp = list(map(int, input().split()))

    for i in range(length-1):
        if temp[i]==0:
            continue
        else:
            if temp[i]==temp[i + 1]:
                temp[i]= 2 * temp[i]
                temp[i + 1]=0

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
    print(ans.strip())
