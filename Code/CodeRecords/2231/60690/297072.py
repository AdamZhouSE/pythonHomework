t=int(input())
res=[]

def isSu(num):
    for i in range(2,num-1):
        if num%i==0:
            return False
    return True

def isSp(num,ele):
    if isSu(num):
        ele.append(num)
        return
    for i in range(2,num):
        if num%i==0 and isSu(i):
            ele.append(i)
            isSp(int(num/i),ele)
            break
    return

for i in range(t):
    n=int(input())
    ele=[]
    isSp(n,ele)
    if len(ele) ==3 and len(set(ele))==3:
        res.append(1)
    else:
        res.append(0)
for e in res:
    print(e)