res = []
for i in range(int(input())):
    output = []
    k = int(input().split()[1])
    array = input().split()
    for j in range(len(array)):
        array[j] = int(array[j])
    array.sort()
    for j in range(k):
        output.append(array[-j-1])
    res.append(output)
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j], end=' ')
    print()