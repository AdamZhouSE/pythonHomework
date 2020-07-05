time=int(input())
str1=input()
list1=str1.split()
size=int(list1[0])
add=int(list1[1])
list1=[]
for i in range(size):
    str2=input()
    li1=str2.split()
    for x in li1:
        list1.append(int(x))
list2=[]
for i in range(size):
    str2=input()
    li1=str2.split()
    for x in li1:
        list2.append(int(x))
count=0
for c in list1:
    for cc in list2:
        if(c+cc==add):
            count+=1
print(count)