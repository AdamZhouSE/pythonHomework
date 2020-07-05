n=int(input())
list=input().split(' ')
str='Yes'
for i in range(0,n):
    while int(list[i])%6==0:
        list[i]=int(list[i])/6
    while int(list[i])%2==0:
        list[i]=int(list[i])/2
    while int(list[i])%3==0:
        list[i]=int(list[i])/3
for i in range(0,n-1):
    if list[i]!=list[i+1]:
        str='No'
        break
    else:
        continue
print(str)