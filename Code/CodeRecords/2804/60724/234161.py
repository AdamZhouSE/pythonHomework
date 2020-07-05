targetstr=input()
list=targetstr.split("+")
num=len(list)
print(list)
list.sort()
print(list)
res=""
i=0
for k in list:
    res=res+k
    i=i+1
    if i!=num:
        res=res+"+"
print(res)