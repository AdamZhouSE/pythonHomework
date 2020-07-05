n=int(input())
str1=input()
str1=str1.split(' ')
str1=list(map(int,str1))
str1.sort()
if(n==1):
    print(str1[0])
else:
    count = 0
    if(str1[0]>=0):
        for i in range(n):
            count+=str1[i]
        ]
        print(count)
    else:
        i=0
        while i<n:
            if(str1[i]>=0):
                x=i
                break
            i+=1
        i=x
        while i<n:
            count+=str1[i]
            i+=1
        j=0
        while j<x:
            count-=str1[j]
            j+=1
        print(count)
            