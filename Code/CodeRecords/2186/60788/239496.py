from sys import stdin

def sum(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s

num=int(stdin.readline().strip())
for i in range(0,num):
    a=int(stdin.readline().strip())
    s=0
    for j in range(1,a+1):
        s+=sum(j)
    print(s)