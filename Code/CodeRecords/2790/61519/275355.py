word=list(input().split(" "))
list1=list(input().split(" "))
list2=list(input().split(" "))
res=[]
num=0
for i in range(len(list2)):
    for j in range(len(list1)):
        if int(list2[i])>=int(list1[j]):
            num=num+1
    res.append(str(num))
    num=0
string=" ".join(res)
print(string)