n=int(input())
str=input()
res="1"
cou=0
for i in range(len(str)):
    if str[i]=='0':
        res+='0'
        cou+=1
if cou==len(str):
    print(0)
else:
    print(res,end='')
