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
leftTmp=0
rightTmp=0
rightFlag=1
flag='left'
while left<=right:
    if flag=='left':
        if leftFlag==0:
            if list1[left][1]<list1[left][0]-list1[left-1][0]:
                count+=1
                left+=1
                flag='right'
            elif list1[left][1]<list1[left+1][0]-list1[left][0]:
                count+=1
                left+=1
                flag='right'
                leftTmp=list1[left][1]
                leftFlag=1
            else:
                left+=1
                flag='right'
                leftFlag=0
        elif leftFlag==1:
            if list1[left][1]<list1[left][0]-list1[left-1][0]-leftTmp:
                count+=1
                left+=1
                flag='right'
                leftFlag=0
            elif list1[left][1]<list1[left+1][0]-list1[left][0]:
                count+=1
                left+=1
                flag='right'
                leftTmp=list1[left][1]
            else:
                left+=1
                flag='right'
                leftFlag=0
    elif flag=='right':
        if rightFlag==1:
            if list1[right][1]<list1[right+1][0]-list1[right][0]:
                count+=1
                right-=1
                flag='left'
            elif list1[right][1]<list1[right][0]-list1[right-1][0]:
                count+=1
                right-=1
                flag='left'
                rightTmp=list1[right][1]
                rightFlag=0
            else:
                right-=1
                flag='left'
                rightFlag=1
        elif rightFlag==0:
            if list1[right][1]<list1[right+1][0]-list1[right][0]-rightTmp:
                count+=1
                right-=1
                flag='left'
                rightFlag=1
            elif list1[right][1]<list1[right][0]-list1[right-1][0]:
                count+=1
                right-=1
                flag='left'
                rightTmp=list1[right][1]
            else:
                right-=1
                flag='left'
                rightFlag=1
print(count)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                