from sys import stdin
def trans(s,t):
    if s%t==0:
        return int(s/t)
    else:
        quoient=int(s/t)
        remainder=s-t*quoient
        dym=""
        while True:
            if 10*remainder%t==0:
                return str(quoient)+'.'+dym+str(int(10*remainder/t))
            a=int(10*remainder/t)
            remainder=(10*remainder)%t
            if dym.count(str(a))==1:
                return str(quoient)+'.'+'('+dym+')'
            else:
                dym+=str(a)

num=int(stdin.readline().strip())
for i in range(0,num):
    p=int(stdin.readline().strip())
    q=int(stdin.readline().strip())
    print(trans(p,q))
                    