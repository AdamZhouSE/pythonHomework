temp=[int(x) for x in input().split(',')]

def equ(li):
    fir=li[0]
    for i in range(len(li)):
        if(li[i]!=fir):
            return False
    return True

count=0
while(not equ(temp)):
    ma=max(temp)
    ind=temp.index(ma)
    for i in range(len(temp)):
        if(i!=ind):
            temp[i]+=1
    count+=1

print(count)