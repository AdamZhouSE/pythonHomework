str=input()
list=str.split(",")
list.sort()
length=len(list)

for i in range(length-1):
    if(list[i]==list[i+1]):
        print(list[i])
        break