T = int(input())
for a in range(0,T):
    n = int(input())
    source=input().split(' ')
    flag = False
    for i in source:
        if source.count(i)>n/2:
            print(i)
            flag = True
            break
    if not flag:
        print(-1)
