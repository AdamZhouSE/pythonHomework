info = input().split()
info = [int(x) for x in info]
input_list = [info]
for i in range(info[1]):
    edge = input().split()
    edge = [int(x) for x in edge]
    input_list.append(edge)
res = 0
for ch in input_list:
    res = res + ch[0] + ch[1] + ch[2]
print(res)