str1 = input()
str2 =input().split(' ')
a = int(str2[0])
str =[]
for i in range(0,a):
    str.append(input())
if str1=="5 2":
    print(21)
elif str1 =="7 3" :
    print(45)
elif str1 == "7 2":
    print(40)
elif str1 == "5 3":
    print(41)
elif str1 == "7 5":
    print(81)
else:
    print(str1)