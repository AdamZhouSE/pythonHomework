info = input().split()
info = [int(x) for x in info]
input_list = [info]
for i in range(info[1]):
    input = input().split()
    input = [int(x) for x in input]
    input_list.append(input)
res = 0
for ch in input_list:
    res = res + ch[0] + ch[1] + ch[2]
print(res)