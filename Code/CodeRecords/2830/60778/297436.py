str1=input().split()
b=int(str1[0])
k=int(str1[1])
a=list(map(int,input().split()))
if(b%2==0):
    if(a[k-1]%2==1):
        print('odd')
    else:
        print('even')
else:
    count=0
    for i in a:
        if(i%2==1):
            count+=1
    if(count%2==1):
        print('odd')
    else:
        print('even')