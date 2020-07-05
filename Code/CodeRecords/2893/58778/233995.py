str=input()
list1=str.split( )
list2=[]
count=0
for y in list1:
    list2.append(int(y))
for i in list2:
    count=count+i
set1=set(list2)
setc=0
for i in set1:
    setc=setc+i
print(int((setc*3-count)/2))