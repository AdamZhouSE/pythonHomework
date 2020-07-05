n = int(input())
l = list(map(int,input().split()))
list1=[]
pre = l[0]
temp = 0
for i in range(n):
    if l[i]!=pre:
        list1.append(temp)
        temp=1
        pre=l[i]
    else:
        temp+=1
    if i==n-1:
        list1.append(temp)
max1=0
for i in range(len(list1)-1):
    if list1[i]=list1[i+1]:
        if list1[i]>max1:
            max1=list1[i]
print(max1*2)
            
    

            
    
    
    