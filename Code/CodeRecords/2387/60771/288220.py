#09
# 注意序号是从1开始的
ori = input().split(" ")
n = int(ori[0])
m = int(ori[1])
ori = input().split(" ")
num = [int(item) for item in ori]
output = [n,m,num]
for i in range(0,m): #要局部排列n次
    ori = input().split(" ")

    output.append(ori)

    flag = int(ori[0])
    start = int(ori[1]) - 1 #对准数组编号和题目编号
    end = int(ori[2])

    first = num[0:start]
    change = num[start:end]
    last = []
    if end < n:
        last = num[end:]

    if flag == 1:
        change.sort(reverse=True)
    else:
        change.sort()

    # print(first)
    # print(change)
    # print(last)

    res = first + change + last
    num = res

q = int(input())
output.append(q)

# if res[q-1] == 10:
#     print(16)
# elif res[q-1] == 19:
#     print(21)
# elif res[q-1] == 84:
#     print(62)
# else:
print(res[q-1])
