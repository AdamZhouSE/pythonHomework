n=int(input())
l1=list(map(int,input().split()[1:]))
l2=list(map(int,input().split()[1:]))
Sum=0
while True:
    if Sum>1000:
        print(l1)
        print(l2)
        break
    if not l1:
        print(Sum,2)
        break
    if not l2:
        print(Sum,1)
        break
    tmp1=l1.pop(0)
    tmp2=l2.pop(0)
    if tmp1>tmp2:
        l1+=[tmp2,tmp1]
    else:
        l2+=[tmp1,tmp2]
    Sum+=1