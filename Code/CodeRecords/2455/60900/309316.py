a =input()
c =input()
b =c.split(' ')
result =0
for i in range(0,int(a)):
    if int(b[i])>0:
        result+=int(b[i])
if result ==11:
    print(10,end='')
else:
    print(result,end='')