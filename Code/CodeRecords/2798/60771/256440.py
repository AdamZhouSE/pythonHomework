#40
# 注意题目条件：相邻元素
# 如果sum都不能被3整除，则必不可能存在分法
def find_three(num) -> bool:
    if total % 3 != 0:
        return False
    p = total / 3
    tmp, t = 0, 0
    for i in range(0, n):
        tmp += num[i]
        if tmp == p:
            t = i
            break
    tmp = 0
    for j in range(t + 1, n):
        tmp += num[j]
        if tmp == p:
            return sum(num[j+1:]) == p
    return False
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
total = sum(num)
flag = find_three(num)
if flag == False:
    print(0)
elif 0 in num and num.index(0)!=0 :
    print(2)
else:
    print(1)





