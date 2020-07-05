T = int(input())
for a in range(0,T):
    N = int(input())
    source = input().split(' ')
    result = []
    for x in source:
        if int(x)%2==0:
            result.append(int(x))
    for x in source:
        if int(x)%2==1:
            result.append(int(x))
    for y in result:
        print(y,end=' ')
    print()