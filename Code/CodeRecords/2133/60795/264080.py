str=input()
arr=[]
for i in range(0,len(str)):
    if str[i]==',':
        continue
    else:
        arr.append(int(str[i]))
number=0
num=len(arr)
max=arr[num-1]-arr[0]
while max>0:
   for i in range(0,num-1):
       arr[i]=arr[i]+1
   number=number+1
   max=max-1
max=arr[num-2]-arr[num-1]
number=number+max
print(number)
