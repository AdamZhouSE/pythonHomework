n=int(input())
for i in range(n):
    s=int(input())
    ss=bin(s)
    x=ss.count('1')
    if(x>1 or x<1):
        print(-1)
    else:
        c=ss.find('1')
        print(len(ss)-c)