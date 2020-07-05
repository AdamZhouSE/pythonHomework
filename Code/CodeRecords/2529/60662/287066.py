n = str(input())
n = "".join((lambda x: (x.sort(), x)[1])(list(n)))
l = len(n)
flag = 0
for i in range(0, 31):
    if len(str(pow(2, i))) == l:
        s = "".join((lambda x: (x.sort(), x)[1])(list(str(pow(2, i)))))
        if s == n:
            print('true')
            flag = 1
            break
if flag == 0:
    print('false')

