n=int(input())
list1=[]
for i in range(0,n):
    tmp=input().split()
    tmp[0]=int(tmp[0])
    tmp[1]=int(tmp[1])
    list1.append(tmp)
count=2
left=1
right=n-2
leftFlag=0
rightFlag=1
flag='left'
while left<=right:
    if flag=='left':
        if leftFlag==0:
            if list1[left][1]<list1[left][0]-list1[left-1][0]:
                count+=1
                left+=1
                flag='right'
            elif list1[left][1]<list1[left][0]-list1[left+1][0]:
                count+=1
                left+=1
                flag='right'
                leftFlag=1
print(list1)