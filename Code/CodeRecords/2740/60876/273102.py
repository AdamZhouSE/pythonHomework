nums=eval(input())
temp=[]
norm=24*60
length=len(nums)
def turn(s):
    a,b=map(int,s.split(":"))
    return a*60+b
for item in nums:
    temp.append(turn(item))
min=norm
for i in range(0,length):
    for j in range(i+1,length):
        gap=temp[i]-temp[j]
        if gap<0:
            gap=-gap
        if gap<min:
            min=gap
        if norm-gap<min:
            min=norm-gap
print(min)