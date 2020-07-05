list1=sorted(eval(input()))
list2=sorted(eval(input()))
result=[]
for item in list1:
    if item in list2:
        result.append(item)
print(result)