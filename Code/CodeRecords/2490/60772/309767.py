def execute(a,b):
    temp = [val for val in a if val in b]
    temp.sort()
    return temp


str = input()
str = str[1:len(str)-1]
li = str.split(",")
a = []
for item in li:
    a.append(int(item))

str2 = input()  # [3,6,9,91]
str2 = str2[1:len(str2)-1]
li2 = str2.split(",")
b = []
for item in li2:
    b.append(int(item))

print(execute(a,b))