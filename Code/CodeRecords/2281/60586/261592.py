def exam8():
    t = int(input())
    result = []
    for i in range(t):
        n = int(input())
        num = []
        for item in input().split(" "):
            num.append(int(item))
        for j in range(1, n):
            if num[j - 1] > num[j]:
                result.append(num[j-1])
                result.append(" ")
        result.append(num[len(num)-1])
        result.append(" ")
        result.append("\n")
    result = result[0:len(result)]
    for item in result:
        print(item, end="")
exam8()