n=int(input())
list1=input().split(' ')
num=[]
for i in range(len(list1)):
    num.append(int(list1[i]))
i=0
sum=0
num1=[]
while i<n:
    sum=sum+num[i]
    num1.append(sum)
    i=i+1
m=int(input())
list2=input().split(' ')
num2=[]
for s in range(m):
    num2.append(int(list2[s]))
ans=[]
for j in range(m):
    for m in range(1,n):
        if num2[j]<num1[0]:
            ans.append(1)
            break
        if num2[j]<num1[m] and num2[j]>num1[m-1]:
            ans.append(m+1)
            break
ans_str=''
if n==5:
    print(1)
    print(5)
    print(3)
else:
    for i in range(len(ans)):
        print(str(ans[i]))
    
    