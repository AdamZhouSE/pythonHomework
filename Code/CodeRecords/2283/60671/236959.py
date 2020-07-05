time=int(input())
while(time>0):
    len=int(input())
    str1=input()
    aarr1=str1.split()
    arr1=[]
    for x in aarr1:
        arr1.append(int(x))
    arr1.sort()
    
    
    
    for x in range(len-1):
        print(str(arr1[x])+" ",end="")
    print(arr1[len-1])
    
    time-=1