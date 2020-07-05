s = input()
t = s.count(',')
list1 = list(s)
for i in range(t):
    list1.remove(',')
list1.remove('[')
list1.remove(']')
list1 = list(map(int, list1))  # python 中字符串list/列表元素转化为数值型/数字
list1.sort()
print(list1)