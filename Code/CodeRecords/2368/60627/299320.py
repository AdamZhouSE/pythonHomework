# 46
n = int(input())
for i in range(n):
    input()
    inp = input()
    num = inp.split()
    for j in range(len(num)):
        num[j] = int(num[j])
    num.sort()
    b = num[:]
    num.sort(reverse=True)
    a = num[:]
    l = []
    
    for i in range(len(num)):
        if i%2 == 0:
            l.append(a[int(i/2)])
        else:
            l.append(b[int(i/2)])
    outp = ''
    for i in l:
        outp += str(i) + ' '
    print(outp[:-1])