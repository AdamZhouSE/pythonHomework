a=eval(input())
lena=len(a)

b=[]
count=0
while count<lena:
    if(a[count]/2!=0):
        b.insert(0,a[count])
    else:
        b.append(a[count])
    count=count+1

print(b)

