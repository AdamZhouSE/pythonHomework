time=int(input())
while(time>0):
    str1=input()
    len1=int(str1[0])
    len2=int(str1[2])
    str2=input()
    aarr1=str2.split()
    arr1=[]
    for x in aarr1:
        arr1.append(int(x))
    str3=input()
    aarr2=str3.split()
    arr2=[]
    for x in aarr2:
        arr2.append(int(x))
    
    isSub=True
    for c in arr2:
        if(c not in arr1):
            isSub=False
    
    if(isSub):
        print("Yes")
    else:
        print("No")
    time-=1
    