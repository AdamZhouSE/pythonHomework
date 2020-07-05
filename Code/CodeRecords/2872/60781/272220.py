n=int(input())
str1=input()
count=0
i=0
while i<n-1:
    if(str1[i]==str1[i+1]):
        count+=1
    i+=1   
print(count)    