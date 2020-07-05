n = int(input())
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
a = b = 0
for i in range(len(l)):
    if i%2==0:
        if l[0]>=l[-1]:
            a += l.pop(0)
        else:
            a += l.pop(-1)
    else:
        if l[0]>=l[-1]:
            b += l.pop(0)
        else:
            b += l.pop(-1)
print (a,b)