size=int(input())
list=input().split()
for i in range(size):
    list[i]=int(list[i])
    while list[i]%3==0:
        list[i]=list[i]//3
    while list[i]%2==0:
        list[i]=list[i]//2
isS=True
for i in range(size-1):
    if list[i+1]!=list[i]:
        isS=False
if isS==False:
    print('No')
else:
    print('Yes')