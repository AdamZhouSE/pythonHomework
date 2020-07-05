t=int(input())
for i in range(t):
    n=int(input())
    list4=input().split(' ')
    count=len(list4)
    ans=0
    for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
                ans=ans+1
    print(ans)
    ans=0