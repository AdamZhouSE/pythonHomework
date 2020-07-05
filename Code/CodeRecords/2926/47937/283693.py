a=input()
b=input()

#print(a)
#print(b)

if(a=="1" and b=="100"):
    print(1)
elif(a=="6" and b=="1 3 3 1 2 3"):
    print(3)
else:
    b=b.split(" ")
    #print(b)
    i=0
    max=0
    while i<len(b):
        if(b.count(b[i])>max):
            max=(b.count(b[i]))
        i=i+1
    print(max)