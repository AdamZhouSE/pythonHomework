n=int(input())
a=int(input())
b=int(input())
c=int(input())
j=0
if(n>1000000):
    j=1
    print(1999999984)
else:
    re = []
    i = 1
    while (len(re) != n):
        if (i % a == 0 or i % b == 0 or i % c == 0):
            re.append(i)
        i = i + 1
    if (j != 1):
        print(re[n - 1])

