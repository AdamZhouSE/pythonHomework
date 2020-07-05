str=input()
arr=[]
for i in range(7,len(str)-1):
    if str[i]==',' or str[i]==' ' or str[i]=='{':
        continue
    
    else:
        arr.append(int(str[i]))
step=0
index=0
while index<len(arr):
    new=[]
    mark=0
    for i in range(index+1,len(arr)):
       if arr[i]==arr[index]:
           mark=1
           new.append(i)
    if mark==1:
        index=new[len(new)-1]
        step=step+1
    else:
        index=index+1
        step=step+1
print(step)