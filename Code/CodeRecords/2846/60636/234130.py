number=int(input(""))
list=input("").split(" ")
result=[]
for i in range(number):
    if(int(list[i])!=0):
        if(not int(list[i]) in result):
            result.append(int(list[i]))
print(len(result))