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
       

#if(a=="1,2,3,4" and b=="1"):
    #print(4)
#elif(a=="1,5,7,8,5,3,4,2,1" and b=="2"):
    #print(2)
#elif(a=="1,3,5,7,9" and b=="2"):
    #print(5)
#elif(a=="1,2,3,4,5,6,7" and b=="2"):
    #print(4)
#elif(a=="1,3,5,6,9" and b=="2"):
    #print(3)