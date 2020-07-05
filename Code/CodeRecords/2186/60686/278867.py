n = int(input())
list_num = []
for i in range(n):
    num = int(input())
    list_num.append(num)
for i in range(n):
    num = list_num[i]
    sum = 1
    for j in range(2, num + 1):
        for k in range(1, j + 1):
            sum += k
    print(sum)
