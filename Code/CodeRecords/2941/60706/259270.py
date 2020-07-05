n=int(input())
str1=input()
list1=list(str1)
sum=0
for i in range(len(list1)):
    if list1[i]=='A':
        sum=sum+4
    elif list1[i]=='B':
        sum=sum+3
    elif list1[i]=='C':
        sum=sum+2
    elif list1[i]=='D':
        sum=sum+1
    else:
        sum=sum+0
str2=str(sum/n)
if sum/n==0:
    print(0,end='')
elif len(str2)<16:
    while len(str2)<16:
        str2=str2+'0'
    print(str2,end='')
else:
    print(round(sum/n,14),end='')