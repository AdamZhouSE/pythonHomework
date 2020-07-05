def exam8():
    t = int(input())
    result = []
    for i in range(t):
        n = int(input())
        num = []
        for item in input().split(" "):
            num.append(int(item))
        for j in range(1, n):
            l=num[j-1]
            for k in range(j,n):
                if l >= num[k]:
                    result.append(num[j - 1])
                    result.append(" ")
        result.append(num[len(num) - 1])
        result.append(" ")
        result.append("\n")
    result = result[0:len(result)]
    for item in result:
        print(item, end="")
exam8()