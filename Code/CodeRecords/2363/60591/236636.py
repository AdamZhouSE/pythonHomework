string = bin(eval(input())).split("0b")[1]
temp = list(string)
for x in range(len(temp)):
    if(temp[x]=='0'):
        temp[x] = '1'
    else:
        temp[x] = '0'
print(eval("0b"+"".join(temp)))