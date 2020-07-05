number=input()
str=input()
list1=str.split(" ")
contain=[]
result=[]
for i in list1:
    contain.append(i)
    length=len(contain)
    for i in range(2**length):
        temp=[]
        for j in range(length):
            if(i>>j)%2:
                temp.append(list1[j])
        result.append(temp)
    print(len(result)-1)
   # print(result)
    result.clear()