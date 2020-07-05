lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
str1=lines.pop(0)
list1=list(eval(str1))
veganFriendly=int(lines.pop(0))
maxPrice=int(lines.pop(0))
maxDistance=int(lines.pop(0))
result=[]
for i in list1:
    if veganFriendly==0:
        if ((i[3]<=maxPrice)&(i[4]<=maxDistance)):
            temp="["+str(i[1])+","+str(i[0])+"]"
            result.append(list(eval(temp)))
    else:
        if ((i[2]==veganFriendly)&(i[3]<=maxPrice)&(i[4]<=maxDistance)):
            temp="["+str(i[1])+","+str(i[0])+"]"
            result.append(list(eval(temp)))
result.sort(reverse=True)
id=[]
for j in result:
    id.append(j[1])
print(id)
