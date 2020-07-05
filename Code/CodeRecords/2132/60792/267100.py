string=input()
num=[]
num.append(string.count("z"))
num.append(string.count("o")-string.count("z")-string.count("w")-string.count("u"))
num.append(string.count("w"))
num.append(string.count("h")-string.count("g"))
num.append(string.count("u"))
num.append(string.count("f")-string.count("u"))
num.append(string.count("x"))
num.append(string.count("s")-string.count("x"))
num.append(string.count("g"))
num.append(string.count("i")-num[6]-num[8]-num[5])
str1=""
for i in range(0,10):
    for j in range(0,num[i]):
        str1=str1+str(i)
print(str1)