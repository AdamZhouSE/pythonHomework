nums=list(input())
num=[]
for i in range(0,len(nums)):
    if nums[i].isdigit():
        num.append(int(nums[i]))
t=num[len(num)-1]
k=num[len(num)-2]
tnum=[]
knum=[]
del num[len(num)-1]
del num[len(num)-1]
if len(num)<k+1 or len(num)<=1:
    print("false")  
else:
    re=1
    for i in range(0,len(num)-1):
        for j in range(i+1,len(num)):
            if abs(num[i]-num[j])==k:
                tnum.append(j-i)
    if len(tnum)==0:
        print("false")
    else:
        if max(tnum)<=k:
            print("true")
        else:
            print("false")
    
        
