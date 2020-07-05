n=int(input())
def panduan(n):
    res=1
    for i in range(32):
        if res>n:
            return False
        elif res==n:
            return True
        else :
            res=res*2
            
for i in range(n):
    a=int(input())
    while not panduan(a):
        a=a+1
    print(a)