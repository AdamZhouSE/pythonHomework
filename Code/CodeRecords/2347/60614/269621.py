init=[int (x) for x in input().split()]
zheng=init[1]
fu=init[0]-init[1]
relationship=[[False]*fu for i in range(zheng)]
while True:
    try:
        temp = [int(x) for x in input().split()]
        relationship[temp[0] - 1][temp[1] - zheng - 1] = True
    except:
        break
partner=[-1]*fu
count=0
def check(zheng,ret):
    for i in range(fu):
        if not ret[1][i] and relationship[zheng][i]==True:
            ret[1][i] = True
            if  ret[2][i]==-1 or check(ret[2][i],ret)[0]:
                ret[0]=True
                ret[2][i]=zheng
                return ret
    ret[0]=False
    return ret
ret=[False,[],partner]
for i in range(zheng):
    visited=[False]*fu
    ret[1]=visited
    if check(i,ret)[0]:
        count+=1
print(count)