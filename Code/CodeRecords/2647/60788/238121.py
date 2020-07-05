from sys import stdin
def f(s):
    if s==0:
        return 0
    if s==1:
        return 1
    t=1
    while True:
        if t<=int(s/2):
            t*=2
        else:
            break
    return f(s-t)+1

num=int(stdin.readline().strip())
for i in range(0,num):
    s=int(stdin.readline().strip())
    print(f(s))