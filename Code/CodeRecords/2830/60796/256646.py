nums=input().split(" ")
b=int(nums[0])
k=int(nums[1])
a=input().split(" ")
a=[int(x) for x in a]
ls=[]
if b%2==1:#b的正整数次方均为奇数
    for i in range(k-1):
        if a[i]%2==1:#奇数×奇数=奇数
            ls.append(1)
        else:#偶数×偶数=偶数
            ls.append(0)
else:
    #b的正整数次方均为偶数
    for i in range(k-1):
            ls.append(0)
if a[k-1]%2==0:
    ls.append(0)
else:
    ls.append(1)

if ls.count(1)%2==0:
    print("even")
else:
    print("odd")



