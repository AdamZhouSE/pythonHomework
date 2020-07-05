str1=input()
str1=str1.split(' ')
str1=list(map(int,str1))
n=str1[0]
h=str1[1]
str2=input()
str2=str2.split(' ')
str2=list(map(int,str2))
count=0
for i in range(n):
    if(str2[i]<=h):
        count+=1
    else:
        count+=2
print(count)