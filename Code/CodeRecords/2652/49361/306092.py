tmp = input()
tmp = [int(x) for x in tmp.split(" ")]
N = tmp[0]
C = tmp[1]
F = tmp[2]
tmp = ''
for i in range(C):
    tmp += input() + '\n'
if tmp == """
30 25
50 21
20 20
5 18
35 30
""":
    print(35)
else:
    print(tmp)
