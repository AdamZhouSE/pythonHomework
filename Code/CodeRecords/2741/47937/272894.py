a=eval(input())
#print(a)
#print(a[0])

max=1

i=0
j=0

while i<len(a):
    j=i+1
    tempmax=1
    while j<len(a):
        if(a[j]>a[i]):
            tempmax=tempmax+1
            j=j+1
            i=i+1
        else:
            i=j
            if(tempmax>max):
                max=tempmax
            break
    i=i+1

print(max)