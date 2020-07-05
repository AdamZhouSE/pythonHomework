n=int(input())
str=input()
list1=str.split( )
temp=[]
for i in list1:
    temp.append(int(i))
count=0
for i in range(1,len(temp)-1):
    if(temp[i-1]>temp[i] and temp[i+1]>temp[i]):
        count=count+1
    if(temp[i-1]<temp[i] and temp[i+1]<temp[i]):
        count=count+1
print(count)
