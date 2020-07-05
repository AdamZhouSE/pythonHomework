n=int(input())
str=input()
list1=str.split( )
temp=[]
for i in list1:
    temp.append(int(i))
count=0
for i in temp:
    count=count+i
if(count%2==0):
    print("YES")
else:
    print("NO")