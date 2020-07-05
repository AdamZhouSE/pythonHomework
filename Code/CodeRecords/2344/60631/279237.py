t = int(input())
for ti in range(t):
    input()
    li = input().split(' ')
    n = int(input())
    lii = li + li
    for i in range(n,n+len(li)):
        print(lii[i],end=' ')
    print()
    #print(lii[n:n+len(li)])