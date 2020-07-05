num=int(input())
for i in range(num):
    line1=list(map(int,input().split(' ')))
    size=line1[0]
    x=line1[1]
    ele=list(map(int,input().split(' ')))
    existed = False
    for a in range(size-1):
        ele1=ele[a]
        for b in range(a+1,size):
            ele2=ele[b]
            if ele1+ele2==x:
                existed=True
    if existed:
        print('Yes')
    else:
        print('No')
