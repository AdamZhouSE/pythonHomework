n=int(input())
str=input()
strlist=str.split()
list1=[]
for i in strlist:
    list1.append(int(i))
list2=[]
j=1
l=0
for i in range(len(list1)-1):
    if(list1[i+1]<=list1[i]*2):
        list2.append(j)
        l=1
        j=j+1
    else:
        j=1
if(l==0):
    print(1)
else:
    print(max(list2)+1)