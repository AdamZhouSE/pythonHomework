# 13
n = int(input())
for i in range(n):
    s = input()
    s_ = ''
    for i in list(s):
        if i=='6':
            s_ += '9'
        else:
            s_ += i
    print(int(s_) -  int(s))