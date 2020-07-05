def decid(num):
    num=int(num)
    ans=[]
    for i in range(1,num):
        if num%i==0:
            ans.append(i)
    return ans

num=int(input())
sum=0
str=decid(num)
for i in range(0,len(str)):
    sum=sum+str[i]
if sum==num:
    print('True')
else:
    print('False')