abc=input()
a=len(abc)
array=list(map(int,abc[1:a-1].split(',')))
array.sort()
i=len(array)-3
flag=True
while i>=0:
    if(array[i]+array[i+1]>array[i+2]):
        print(array[i]+array[i+1]+array[i+2])
        flag=False
        break
    i-=1
if(flag):
    print("0")