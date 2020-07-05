list1=list(map(str,input()[1:-1].split(",")))
list2=list(map(str,input()[1:-1].split(",")))
for num1 in list1:
    if(num1.isdigit()==False and num1.startswith("-")==False):
        list1.remove(num1)
for num2 in list2:
    if(num2.isdigit()==False and num2.startswith("-")==False):
        list2.remove(num2)
list3=[int(i) for i in list1]+[int(j) for j in list2]
list3.sort()
print(list3)
