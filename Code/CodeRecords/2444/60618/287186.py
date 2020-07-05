nums=list(input())
num=[]
for i in range(0,len(nums)):
    if nums[i].isdigit():
        num.append(int(nums[i]))
t=num[len(num)-1]
k=num[len(num)-2]
del num[len(num)-1]
del num[len(num)-1]
if len(num)<k+1:
    print("false")
else:
    re=1
    for i in range(0,len(num)-k):
        if abs(num[i]-num[i+k])==t:
            print("true")
            re=0
            break
    if re==1:
        print("false")
        
