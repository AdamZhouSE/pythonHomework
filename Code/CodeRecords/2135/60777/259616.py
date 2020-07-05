temp=[int(x) for x in input().split(',')]

def ma(li):
    mo=max(li)
    su=0
    for i in li:
        su+=(mo-i)
    return su

def mi(li):
    lea=min(li)
    su=0
    for i in li:
        su+=(i-lea)
    return su
        
def equ(li):
    fir=li[0]
    for x in li:
        if(x!=fir):
            return False
    return True
count=0
while(not equ(temp)):
    if(ma(temp)<=mi(temp)):
        ind=temp.index(min(temp))
        temp[ind]+=1
        count+=1
    else:
        ind=temp.index(max(temp))
        temp[ind]-=1
        count+=1
        
print(count)