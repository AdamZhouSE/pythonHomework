T = int(input())
for a in range(0,T):
    N = int(input())
    source = input().split(' ')
    result = ""
    for i in source:
        if i!='0':
            result = result+i+" "
    for j in range(len(result)//2,N):
        result = result+"0 "
    print(result)
