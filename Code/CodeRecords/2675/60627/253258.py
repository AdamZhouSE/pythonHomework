# 13
n = int(input())
for i in range(n):
    s = input()
    s_ = ''
    for i in list(s):
        if i=='6':
            s += '9'
        else:
            s += i
    print(int(s_) -  int(s))