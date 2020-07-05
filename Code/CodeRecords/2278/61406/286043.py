T = int(input())
for a in range(0,T):
    n = int(input())
    source = input().split(' ')
    result = ""
    for i in range(0,n-1):
        result=result+str(int(source[i])^int(source[i+1]))+" "
    result = result+source[n-1]
    print(result)


