str = input()

list = list(str)

for j in range(0,len(list)-1):
    for i in range(0,len(list)-1-j):
        if list[i]>list[i+1]:
            temp=list[i]
            list[i]=list[i+1]
            list[i+1]=temp

for i in range(0,len(list)):
    print(list[i],end="")
print("")