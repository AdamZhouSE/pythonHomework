import re
n=input()
n=n[1:len(n)-1]
list=re.split(r'[\[\],\t]',n)
list=[i for i in list if i!='']
li=[]
for i in range(len(list)):
    li.append(int(list[i]))
m=0
for i in range(0,len(li)-1):
    for k in range(i+1,len(li)):
      if(int(li[i])>int(li[k])):
          m=li[i]
          li[i]=li[k]
          li[k]=m
arr=''
for i in range(len(li)):
    arr=arr+", "+str(li[i])
print('['+arr[2:len(arr)]+']')