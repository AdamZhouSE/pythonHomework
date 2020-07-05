nums=input().split(",")
res=[]
for x in nums:
    res.append(int(x))
res=sorted(res)
maxvalue=res[-1]*res[-2]*res[-3]
print(maxvalue)