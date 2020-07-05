list1=input().split(' ')
n=int(list1[0])
d=int(list1[1])
list2=input().split(' ')
ans=0
temp=0
num=[]
for i in range(0,len(list2)):
    num.append(int(list2[i]))
for i in range(0,len(num)-1):
    if num[i]>=num[i+1]:
        temp=int((num[i]-num[i+1])/d)+1
        ans=ans+temp
        num[i+1]=num[i+1]+temp*d
        
print(ans)
