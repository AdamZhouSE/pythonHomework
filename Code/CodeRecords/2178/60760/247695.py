number=input()
str=input()
list1=str.split(" ")
contain=[]
result=[]
for i in list1:
    contain.append(i)
    length=len(contain)
    father="".join(contain)
    for j in range(1,length+1):
        for n in range(length-j+1):
            son=father[n:n+j]
            result.append(son)
    print(len( set(result)))
    result.clear()