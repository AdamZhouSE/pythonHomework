str=input()
arr=[]
for i in range(0,len(str)):
    if str[i]==',':
        continue
    else:
        arr.append(int(str[i]))
number=0
num=len(arr)
index=num//2
for i in range(0,index):
    number=number+arr[index]-arr[i]
for j in range(index+1,num):
    number=number+arr[j]-arr[index]
print(number)
