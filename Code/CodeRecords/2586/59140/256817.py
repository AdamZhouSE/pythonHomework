a=int(input())
b=int(input())
c=int(input())
num=[a,b,c]
num.sort()
x,y,z=num[0],num[1],num[2]
max = (y-x-1)+(z-y-1)
if y-x-1==0 and z-y-1==0:min=0
elif min(y-x-1,z-y-1)<2:min=1
else:min=2
result=[min,max]
print(result)