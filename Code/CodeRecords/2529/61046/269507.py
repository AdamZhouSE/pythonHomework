numIn = input()
str1 = sorted(numIn)
list = []
res = 'false'
for i in range(0,32):
    num = pow(2,i)
    numstr = sorted(str(num))
    list.append(numstr)
for x in list:
    if x == str1:
        res = 'true'
        break
print(res)