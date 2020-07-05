str = input()
str = str.replace("[", "")
str = str.replace("]", "")
list1 = str.split(",")
for i in range(len(list1)-1):
    for j in range(len(list1)-i-1):
        if int(list1[j]) > int(list1[j+1]):
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
int_list = list(map(int, list1))    #转化为int型数组
print(int_list)