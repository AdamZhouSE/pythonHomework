inp = int(input())
str1 = ""
res = 0
while(inp!=0):
    remainder = inp % 2
    inp = inp // 2
    if(remainder==1):
        str1 += "0"
    else:
        str1 += "1"
str1 = str1[::-1]
for i in range(len(str1)):
    res = res+ int(str1[i])*pow(2,len(str1)-1-i)
print (res)