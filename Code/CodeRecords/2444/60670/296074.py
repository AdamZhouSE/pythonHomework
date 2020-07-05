t=input().split("],")
nums=eval(t[0][7:]+']')
t=t[1].split(',')
k=int(t[0][5:])
t=int(t[1][5:])
finded=False
for m in range(1,k+1):
    for i in range(0,len(nums)-k):
        if abs(nums[i+m]-nums[i])<=t:
            finded=True
            break
    if finded:
        break
if finded:
    print("true")
else:
    print("false")