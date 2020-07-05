def solve(a, b):
    res = 0
    for i in range(b):
        res = res + i
        if a-res < i+1:
            return 0
    return 1


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = input().split(" ")
    result.append(solve(int(num[0]),int(num[1])))
for i in result:
    print(i)