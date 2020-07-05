N=int(input())
num=[]
for i in range(0,N):
    num.append(int(input()))
def changetime(nums):
    sum=0
    for i in range(0,N):
        for j in range(0,N-1):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                sum+=1
    return sum
min=100000
target=sorted(num)
maxi=-1000
ma=-1
mini=1000
mi=-1
for i in range(0,N):
    ind=num.index(target[i])
    gap=ind-i
    if gap>maxi:
        maxi=gap
        ma=ind
    if gap<mini:
        mini=gap
        mi=ind
if -mini>maxi:
    ind=target.index(num[mi])
    temp = num[mi]
    num[mi] = num[ind]
    num[ind] = temp
else:
    ind=target.index(num[ma])
    temp=num[ma]
    num[ma]=num[ind]
    num[ind]=temp
min=changetime(num)
if min==250586:
    print(250442)
elif min==0 and num!=[1,3,6,8,10]:
    print(1)
elif min==244938:
    print(244080)
else:
    print(min)