n=int(input())
str1=input()
str1=str1.split(' ')
str1=list(map(int,str1))
str1.sort()
count=0
for i in range(n):
    count+=str1[i]
if(count%2==0):
    print(count)
else:
    for i in range(n):
        if((count-str1[i])%2==0):
            print(count-str1[i])
            break