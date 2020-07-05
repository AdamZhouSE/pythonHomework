n,m = input().split()
n = int(n)
m = int(m)
num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])
for i in range(m):
    x,a,b= input().split()
    a = int(a)
    b = int(b)
    x = int(x)
    if x==0:
        re = False
    else:
        re = True
    l = num[a-1:b]
    l.sort(reverse = re)
    num = num[0:a-1] +l + num[b:]
n = int(input())
print(num[n-1])