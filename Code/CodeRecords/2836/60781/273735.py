n=int(input())
str1=input()
str1=str1.split(' ')
l=str1
l=list(map(int,l))
str1=list(map(int,str1))
str1.sort()
if(str1==l):
    print('0')
else:
    pan=0
    for i in range(n):
        if(l[n-1]==str1[0] and l[0:n-1]==str1[1:n]):
            print(i+1)
            pan=1
            break
        else:
            temp=l[n-1]
            l[1:n]=l[0:n-1]
            l[0]=temp
    if(pan==0):
        print('-1')

