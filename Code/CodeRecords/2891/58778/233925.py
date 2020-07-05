n=int(input())
str=input()
list1=str.split( )
temp=[]
for i in list1:
    temp.append(int(i))
j=max(temp)
count=0
for i in temp:
    count=count+i
print(j*n-count)