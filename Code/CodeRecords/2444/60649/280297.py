import re
s=input()
s2=re.search('\[(\d,){1,}\d\]',s)
nums=eval(s2.group())
s2=re.findall('\w\s=\s(\d+)',s)
k,t=int(s2[0]),int(s2[1])
f=False
for i in range(len(nums)-k):
    for j in range(i+1,i+k+1):
        if abs(nums[i]-nums[j])<=t:
            print("true")
            f=True
            break
    if f:
        break
else:
    print("false")
#正则表达式解析 然后暴力

