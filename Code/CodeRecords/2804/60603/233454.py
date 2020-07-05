str=input()
list=str.split("+")

for i in list:
    i=int(i)
list.sort()

for i in range(0,len(list)):
    if(i==(len(list)-1)):
        print(list[i])
        break
    print(list[i]+"+",end="")