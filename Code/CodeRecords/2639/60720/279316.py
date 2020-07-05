str1=input()
k=int(input())
max=0
for i in range(len(str1)):
    temp=k
    sum=1
    index=i+1
    s=str1[i]
    if len(str1)-index+1<=max:
        break
    while(temp>0 and index<len(str1)):
        if str1[index]!=s:
            temp-=1
        sum+=1
        index+=1
    while index<len(str1):
        if str1[index]==s:
            sum+=1
        else:
            break
        index+=1
    if sum>max:
        max=sum
print(max)
