str1 = input()
a1,b1 = '',''
str2 = input()
a2,b2 = '',''
for i in range(len(str1)):
    if str1[i]=='+':
        a1 = str1[0:i]
        b1 = str1[i:len(str1)-1]
for i in range(len(str2)):
    if str2[i]=='+':
        a2 = str2[0:i]
        b2 = str2[i:len(str2)-1]
#print("{} {} {} {}".format(a1,b1,a2,b2))
x1 = int(a1)
y1 = int(b1)
x2 = int(a2)
y2 = int(b2)
part_1 = x1*x2 - y1*y2
part_2 = x1*y2 + x2*y1
print("{}+{}i".format(part_1,part_2))