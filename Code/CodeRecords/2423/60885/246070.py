def test():
    M,N = list(map(int, input().split()))
    arr1 = sorted(list(map(int, input().split())))
    arr2 = sorted(list(map(int, input().split())))
    i2 = 0
    for i1 in range(len(arr1)):
        if arr1[i1] == arr2[i2]:
            i2 += 1
        if i2 == len(arr2):
            result.append('Yes')
            return
    result.append('No')

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)