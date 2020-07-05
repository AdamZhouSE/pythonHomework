t = int(input())
for i in range(0,t):
    data = int(input())
    result = 0
    for i in range(1,data + 1):
        result = result + pow(i,5)
    print(result)