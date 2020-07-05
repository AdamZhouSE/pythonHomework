# 1
inp = input()
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])

d = int(input())

l = []
if len(num) > int(2**(d-1)-1):
    if len(num) <= int(2**(d-1)-1) +int(2**(d-1)) :
        l = num[int(2**(d-1)-1):]
    else:
        l = num[int(2**(d-1)-1):int(2**(d-1)-1) +int(2**(d-1))]
    outp = ''
    for i in l:
        outp += str(i) + ' '
    print(outp[:-1])
if len(l) == 0:
    print('EMPTY')