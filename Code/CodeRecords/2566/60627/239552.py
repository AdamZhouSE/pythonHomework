# 20
n = int(input())
s = '['
for i in range(n):
    inp = input()
    s += ('[' + inp + '],')
s = s[:-1] + ']'
from ast import literal_eval
num = literal_eval(s)
print(num)