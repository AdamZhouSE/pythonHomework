def com(a):
    arr=a
    ar=""
    for i in range(0,len(a)-1):
        ch=str((int(arr[i])+int(arr[i+1]))%10)
        #print(ch)
        ar=ar+ch
        #print(ar)
    return ar

arr=input()
num=int(input())
ar=""
for a in arr:
    ar=ar+str(ord(a)-ord('A')+num)
length=len(ar)
b=0
#print(ar)
array=ar
for i in range(0,length):
    array=com(array)
    #print(array)
    if(int(array)<=100):
         break
if(array[0]=='0'):
    array=array[1:]
print(array.lstrip(),end='')