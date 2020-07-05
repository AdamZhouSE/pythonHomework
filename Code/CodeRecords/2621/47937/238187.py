a=eval(input())
max=-99999
l=len(a)
#print(a)
#print(l)
#print(a[0])
i=0
while i<l:
    i2=i
    tempnum=0
    while i2<l:
        tempnum=tempnum+a[i2]
        if(tempnum>max):
            max=tempnum
        i2=i2+1
    i=i+1
print(max)

