n=eval(input())
bstr=input()
num1=0
num0=0
for i in range(n):
    if bstr[i]=='1':
        num1+=1
    else:
        num0+=1
if num1==0:
    print(0,end='')
else:
    res='1'
    for i in range(num0):
        res+='0'
    print(res,end='')