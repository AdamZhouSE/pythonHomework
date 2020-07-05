k=int(input())
for i in range(0,k):
    n=int(input())
    m=n
    list4=input().split(' ')
    count=len(list4)
    for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
    for i in range(0,n):
        if int(list4[n-m])<m:
            m=m-1
    print(m)