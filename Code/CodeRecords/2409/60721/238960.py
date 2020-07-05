import re
nums=re.findall(r"[0-9]{1,}",input())
nums=[int(i) for i in nums]
m=0
n=0
for x in nums:
    if(x%2==0):m+=1
    else:n+=1
print(min(m,n))