num=int(input())
for nn in range(num):
    n=int(input())
    s=list(map(int, input().split()))
    f=list(map(int, input().split()))
    l=list(enumerate(zip(s,f)))
    l.sort(key=lambda x:x[1][1])
    i = 0
    print(l[0][0]+1, end = " ")
    for j in range(1,len(l)):
        if (l[j][1][0] >= l[i][1][1]):
            print(l[j][0] + 1, end = " ")
            i = j
    print()

