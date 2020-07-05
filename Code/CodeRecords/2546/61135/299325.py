T=int(input())
def p(x):
    if(x==0 or x==1 or x==2):
        return 1
    else:
        return p(x-2)+p(x-3)
for a in range(0,T):
    num=int(input())
    print(p(num))