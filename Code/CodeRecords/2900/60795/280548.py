arr=input()
num=0
for i in range(0,len(arr)):
    if arr[i]==' ':
        continue
    elif arr[i]=='\n':
        continue
    else:
        num+=1

print(num,end="")