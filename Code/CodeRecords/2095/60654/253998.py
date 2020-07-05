a = int(input())
b = int(input())
c = list(str(a+b))
c.insert(0 , "0")
s = ""
sign = 0
for i in range(c.__len__()-1 , -1 , -1):
    temp = sign
    sign = (temp+int(c[i]))//2
    s = str((temp+int(c[i]))%2) + s
print(s)