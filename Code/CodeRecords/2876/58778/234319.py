n=int(input())
str=input()
list1=str.split( )
temp=[]
for i in list1:
    temp.append(int(i))
if temp[0]==0:
    del temp[0]
if temp[len(temp)-1]==0:
    del temp[len(temp)-1]

c=0
for i in range(1,len(temp)-1):
    if(temp[i]==0 and (temp[i-1]==1 and temp[i+1]==1)):
        
            c=c+1
            temp[i+1]=0

print(c)