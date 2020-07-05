def judge(list_temp, res):
    div = int(len(list_temp) / res)
    for a in range(div):
        for b in range(int(res / 2)):
            list_temp[a * res + b], list_temp[(a + 1) * res - b - 1] = list_temp[(a + 1) * res - b - 1], list_temp[a * res + b]
    temp = len(list_temp) % res
    for a in range(int(temp / 2)):
        list_temp[res * div + a], list_temp[len(list_temp) - 1 - a] = list_temp[len(list_temp) - 1 - a], list_temp[
            res * div + a]
    for a in range(len(list_temp)):
        print(list_temp[a], end=" ")
    print()


num = int(input())
list_all = []
list_num = []
for i in range(num):
    n, m = (int(x) for x in input().split(" "))
    list_num.append(m)
    list_input = input().split(" ")
    for j in range(n):
        list_input[j] = int(list_input[j])
    list_all.append(list_input)
for x in range(num):
    judge(list_all[x], list_num[x])
