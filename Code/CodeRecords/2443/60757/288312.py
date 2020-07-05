def so(s1,s2):
    if s1+s2>s2+s1:
        return True
    else:
        return False
arr=eval(input())
for i in range(len(arr)-1):
    for j in range(0,len(arr)-i-1):
        if not(so(str(arr[j]),str(arr[j+1]))):
            tmp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=tmp
for i in range(len(arr)):
    print(str(arr[i]),end='')
print()