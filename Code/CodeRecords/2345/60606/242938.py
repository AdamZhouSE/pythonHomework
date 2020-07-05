test_num = int(input())
result = []
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    sumAll = (1+n)*n/2
    sumShort = 0
    set1 = set()
    sumLong = 0
    for j in array:
        sumLong += j
        set1.add(j)
    for j in set1:
        sumShort += j
    result.append(int(sumLong - sumShort))
    result.append(int(sumAll - sumShort))
    result = [str(x) for x in result]
    print(" ".join(result))
    result.clear()

