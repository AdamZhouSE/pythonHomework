i = 0
str0 = input()

nums = []
op =[]
k=0
n = 0
while(k!=len(str0)):
    if str0[k]=='/':
        if n==0:
            if str0[0]=='-':
                op.append(-1)
                nums.append([int(str0[k - 1]), int(str0[k + 1])])
                n+=1
            else:
                op.append(1)
                nums.append([int(str0[k - 1]), int(str0[k + 1])])
                n+=1
        else:
            if str0[k-2]=='+': op.append(1)
            else: op.append(-1)
            n+=1
            nums.append([int(str0[k - 1]), int(str0[k + 1])])
    k+=1

count =1
for i in range(0,len(nums)):
    count*=nums[i][1]
temp =0
for i in range(0,len(nums)):
    temp+=int(((nums[i][0])*count/nums[i][1])*op[i])

for i in range(2,min(temp,count)+1):
    if temp%i==count%i==0:
        temp=int(temp/i)
        count = int(count/i)
 
for i in range(2,min(temp,count)+1):
    if temp%i==count%i==0:
        temp=int(temp/i)
        count = int(count/i)
        
if temp==0:
    print("0/1")
elif temp%count==0:
    print(int(temp/count),end='')
    print("/1")
else:
    print(temp,end='')
    print("/",end='')
    print(count)