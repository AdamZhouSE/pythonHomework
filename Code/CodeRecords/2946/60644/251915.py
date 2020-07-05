str=input()
res=0
arr=str.split('1')
for i in range(0,len(arr)):
    if arr[i].count('0')>=1:
        arr[i]=3
if str[0:1]=='0':
    print(1,end="")
else:
    print(arr.count(3)*2,end="")

