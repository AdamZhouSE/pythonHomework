s=input().split(" ")
nums=eval(s[2][0:len(s[2])-1])
k=s[5][0:len(s[5])-1]
k=int(k)
t=s[8]
t=int(t)
for i in range(len(nums)):
    nums[i]=int(nums[i])
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
