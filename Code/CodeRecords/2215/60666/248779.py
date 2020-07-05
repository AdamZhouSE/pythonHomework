nums=list(map(int,input().strip().split(",")))
num=[]
for n in nums:
    num.append(str(n))
result=num[0]+"/("
for i in range(1,len(num)-1):
    result+=num[i]+"/"
result+=num[len(num)-1]+")"
print(result)