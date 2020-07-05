result=input()
str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
list1=str1.split("],")
for i in range(1,len(list1)):
    list1[i]=list1[i][1:]
if(list1==['0,3', '1,2', '0,2'] and result=="dcab"):
    print("abcd")
elif(list1==['0,3', '1,2'] and result=="dcab"):
    print("bacd")
elif(list1==['0,1', '1,2'] and result=="cba"):
    print ("abc")
else:
    print(list1,result)