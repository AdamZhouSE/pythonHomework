temp = input()
temp = temp.replace(" ","")
temp = temp.replace("=","")
s = temp.split(",")[0][1:]
t = temp.split(",")[1][1:]
a = list(s)
a.sort()
b = list(t)
b.sort()
flag = 1
for i in range (0,len(a)):
    if(a[i]!=b[i]):
        flag = 0
if(flag == 1):
    print("true")
else:
    print("false")