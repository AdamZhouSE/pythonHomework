n=int(input())
def panduan(n):
    strr=str(n)
    c=1
    for i in range(1000):
        res=0
        for j in range(len(strr)):
            res+=int(strr[j])*int(strr[j])
        n=res
        strr=str(n)
        if res==1:
            c=0
            break
    if c==0:
        return True
    else:
        return False
for i in range(n):
    a=int(input())
    while not panduan(a+1):
        a=a+1
    print(a+1)