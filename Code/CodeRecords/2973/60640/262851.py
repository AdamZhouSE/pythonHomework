"""
取读入字符串的每个8位的子串，判断其中各个字符的数量是否与密码的对应相等
"""
inp = input()
# 连续8位的子串个数
amount = len(inp)-8+1
sub = []
for i in range(amount):
    sub_str = list(inp[i:i+8])
    # 获取8位子串中不同的元素，组成一个列表，并按照升序排列
    element = sorted(list(set(sub_str)))
    element_num = []
    # 对应元素的数量
    for j in range(len(element)):
        element_num.append(sub_str.count(element[j]))
    sub.append([element, element_num])
n = int(input())
res = 0
for i in range(n):
    inp = list(input())
    # 输入密码中不同的元素组成列表，并排序
    set_inp = sorted(list(set(inp)))
    inp_num = []
    # 不同元素对应的数量
    for j in range(len(set_inp)):
        inp_num.append(inp.count(set_inp[j]))
    for k in range(len(sub)):
        if set_inp == sub[k][0] and inp_num == sub[k][1]:
            res += 1
print(res)
