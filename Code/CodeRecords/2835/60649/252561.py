from  collections import Counter
n=int(input())
a=list(map(int,input().split()))
count=Counter(a)
nof5=count[5]
nof0=count[0]
num=0
if nof0==0:
    print(-1)
else:
    for i in range(nof5):
        if ((nof5-i)*5)%9==0:
            num=nof5-i
            break
    if num==0:
        print(0)
    else:
        str="5"*num+"0"*nof0
        print(int(str))
