times = int(input())
for i in range(times):
    num = int(input())
    result = []
    for j in range(num+1):
        if j & num == j:
            result.append(j)
    for k in range(1,len(result)):
        print(result[len(result)-k],"",end="")
    print(result[0],"")
