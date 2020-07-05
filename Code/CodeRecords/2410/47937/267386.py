a=input().split(",")
b=input()



#print(len(a))

c=[]
i=0
while i<len(a):
    c.append(int(a[i]))
    i=i+1
    
#print(c)

d=int(b)

i=0

end=1

while i<len(a):
    length=1
    i2=i+1
    i3=i
    while i2<len(a):
        if(c[i2]-c[i3]==d):
            i3=i2
            i2=i2+1
            length=length+1
            continue
        i2=i2+1
    if(length>end):
        end=length
    i=i+1
print(end)
