nums=eval(input())
k=int(input())
t=int(input())
length = len(nums)
a=0
if t == 0 and len(set(nums)) == length:
    print("false" )
    a=-1
for i in range(length):
    for j in range(i+1,length):
        if j - i <= k and abs(nums[i]-nums[j]) <= t:
            if a!=-1:
                print("true")
                a=-1
if a!=-1:
    print("false")
