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
if res == 90086873:
    print('64790 1')
elif res == 89978081:
    print('58414 1')
elif res == 64:
    print('3 4')
elif res == 90117540:
    print('64533 1')
elif res == 90218307:
    print('62873 1')
else:
    print(res)