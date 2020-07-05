def cal(index):
    if index == 1:
        return 1
    if index == 0:
        return 2
    if index > 1:
        return cal(index - 1) + cal(index - 2)


n = int(input())
list_num = []
for i in range(n):
    num = int(input())
    list_num.append(num)
for i in range(n):
    num = list_num[i]
    print(cal(num) % 1000000007)
