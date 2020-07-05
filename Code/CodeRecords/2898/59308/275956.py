l = int(input())
s = input()
if s == '0':
    print(0)
else:
    print(1, end='')
    s_ = 0
    for i in range(0, l):
        if s[i] == '0':
            s_ += 1
    for i in range(1, s_ + 1):
        print(0, end='')

