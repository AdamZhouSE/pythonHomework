nums=eval(input())
def larger(a,b):
    bita=0
    bitb=0
    tempa=[]
    tempb=[]
    while a>0:
        tempa.append(a%10)
        a=a//10
        bita+=1
    while b>0:
        tempb.append(b%10)
        b=b//10
        bitb+=1
    tempa.reverse()
    tempb.reverse()
    if tempa[0]>tempb[0]:
        return True
    elif tempa[0]<tempb[0]:
        return False
    bita-=1
    bitb-=1
    ind=1
    while bita>0 and bitb>0:
        if tempa[ind]>tempb[ind]:
            return True
        elif tempa[ind]<tempb[ind]:
            return False
        ind+=1
        bita-=1
        bitb-=1
    if bita>0:
        if tempa[ind]>=tempa[0]:
            return True
        else:
            return False
    if bitb>0:
        if tempb[ind]>=tempb[0]:
            return False
        else:
            return True
    return True
length=len(nums)
for i in range(0,length):
    max=i
    for j in range(i,length):
        if larger(nums[j],nums[max]):
            max=j
    temp=nums[i]
    nums[i]=nums[max]
    nums[max]=temp
sum=0
for item in nums:
    if item<10:
        sum*=10
    elif item<100:
        sum*=100
    elif item<1000:
        sum*=1000
    elif item<10000:
        sum*=10000
    elif item<100000:
        sum*=100000
    elif item<1000000:
        sum*=1000000
    else:
        item*=10000000
    sum+=item
print(sum)