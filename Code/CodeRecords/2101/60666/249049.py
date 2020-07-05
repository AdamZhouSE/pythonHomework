n=int(input())
dict={}
sum=0
flag=True
while sum!=1:
    sum=0
    for i in str(n):
        sum+=int(i)**2
    n=sum
    if n not in dict:
        dict[n]=1
    else:
        flag=False
if flag==True:
    print(flag)
else:
    print(False)