def mul(result,arr1,arr2):
    for x in range(len(arr1)):
        for y in range(len(arr2)):
            result[x+y] += (arr1[x] * arr2[y])
    return result

n = eval(input())
while(n!=0):
    lens = sum(list(map(int,input().split(" "))))
    result = []
    while(lens > 1):
        lens -= 1
        result.append(0)
    arr1 = list(map(int,input().split(" ")))
    arr2 = list(map(int,input().split(" ")))
    res = list(map(str,mul(result,arr1,arr2)))
    print(" ".join(res))