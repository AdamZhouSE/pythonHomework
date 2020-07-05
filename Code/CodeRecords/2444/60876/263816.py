string=list(map(str,input().split(" ")))
nums=eval(string[2][0:len(string[2])-1])
k=int((string[5])[0:len(string[5])-1])
t=int(string[8])
length=len(nums)
jud=False
for i in range(0,length-k):
    if nums[i]-nums[i+k]<=t and nums[i+k]-nums[i]<=t:
        print("true")
        jud=True
        break
if not jud:
    print("false")