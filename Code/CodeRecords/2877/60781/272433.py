n=int(input())
str1=input()
str1=str1.split(' ')
str1=list(map(int,str1))
str1.sort()
if(n==1):
    print(str1[0])
else:
    count=0
    for i in range(n):
        count+=str1[i]
count=count-2*str1[0]
print(count)
