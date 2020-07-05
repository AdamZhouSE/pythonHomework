str=input()
list=str.split("+")
print("hah")
for i in list:
    i=int(i)
list.sort()
print(len(list))
for i in range(0,len(list)):
    if(i==(len(list)-1)):
        print(list[i],end="")
        break
    print(list[i]+"+",end="")