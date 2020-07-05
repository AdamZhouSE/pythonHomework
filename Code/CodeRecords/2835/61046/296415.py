num=int(input())
test=input().split()
test=list(map(int,test))
count5=0
count0=0
for x in test:
    if x==5:
        count5+=1
    else:
        count0+=1
if(count5>=9 and count0>=1):
    while count5>=9:
        if(count5%9==0):
            break
        else:
            count5-=1
    print('5'*count5+'0'*count0)
elif count0>0:
    print(0)
else:
    print(-1)