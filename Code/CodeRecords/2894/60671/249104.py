length=int(input())
str1=input()
count=0
for i in range(length-1):
    if(str1[i]=='V' and str1[i+1]=='K'):
        count+=1
for i in range(length-1):
    if(str1[i]=='K' and str1[i+1]=='K')or(str1[i]=='V' and str1[i+1]=='V'):
        count+=1
        break
print(count,end='')