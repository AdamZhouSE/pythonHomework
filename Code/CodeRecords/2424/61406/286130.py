T = int(input())
for a in range(0,T):
    n = int(input())
    source = input().split(' ')
    flag = False
    for i in source:
        if source.count(i)%2==1:
            print(i)
            flag = True
            break
    if not flag:
        print(0)
        