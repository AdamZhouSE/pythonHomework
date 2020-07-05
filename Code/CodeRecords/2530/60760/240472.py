str1=input()
str2=input()
list1=[]
for i in str1:
    list1.append(str2.count(i))
str3=list(str2)
for i in str2:
    if i in str1:
        str3.remove(i)
number=0
for i in str1:
    for j in range(list1[number]):
        print(i,end="")
    number=number+1
print(",".join(str3))