str=input()
str1=str.split(" ")
for i in range(len(str1)-1):
    print(str1[len(str1)-2-i]+" ",end="")