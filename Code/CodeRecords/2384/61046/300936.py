num=int(input())
length=[]
test=[]
for i in range(num):
    length.append(input())
    test.append(input())
for i in range(num):
    now=test[i].split()
    now=list(map(int,now))
    now=sorted(now)
    nowi=[]

    for x in now:
        if x>0:
            nowi.append(x)
    ans=len(nowi)+1
    for i in range(1,len(nowi)+1):
        if i!=nowi[i-1]:
            ans=i
            break
    print(ans)