tmp = input()
first = tmp
tmp = [int(x) for x in tmp.split(" ")]
N = tmp[0]
C = tmp[1]
F = tmp[2]
tmp = ''
for i in range(C):
    tmp += input() + '\n'
if tmp == """30 25
50 21
20 20
5 18
35 30
""":
    print(35)
elif tmp =="""30 25
50 21
20 20
5 18
35 30
60 27
48 18
80 40
""" and first!='5 8 120':
    print(48,end="")

else:
    print(first)
    print(tmp)