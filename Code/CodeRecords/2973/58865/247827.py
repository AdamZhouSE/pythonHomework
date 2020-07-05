s = input()  # 密文
n = int(input())  # 密码个数
password = []  # 密码列表
for i in range(n):
    password.append(input())


# 全排列算法
def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]

def permutation(stra, point):
    length = len(stra)
    lsta = list(stra)
    if point == length:
        strout=''.join(lsta)
        if strout not in arr:
            arr.append(strout)
        return arr
    for i in range(point, length):
        swap(lsta, i, point)
        s=''.join(lsta)
        permutation(s, point + 1)
        '''第i位后面全排列交换之后，换回原序列。
        比如给定1234，1和2交换变成2134，
        上行全排列交换之后，需换回换回1234继续1和3交换'''
        swap(lsta,i,point)


count = 0

for i in password:
    arr = []  # 存放全排列结果
    permutation(i, 0)
    for j in arr:
        if j in s:
            count+=1
print(count)
