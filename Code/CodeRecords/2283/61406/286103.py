T = int(input())
for a in range(0,T):
    n = int(input())
    source = input().split(' ')
    source.sort()
    result = ""
    for i in source:
        result = result+i+" "
    print(result.rstrip(' '))
    