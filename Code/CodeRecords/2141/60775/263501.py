def do(n:int):
    tmp = ''
    while n != 0:
        tmp += str(n%2)
        n = n//2
    result = ''
    for i in range(len(tmp)):
        result = tmp[i] + result
    print(result+' ',end='')

test = int(input())
for i in range(test):
    n = int(input())
    for j in range(1,n+1):
        do(j)
    print()