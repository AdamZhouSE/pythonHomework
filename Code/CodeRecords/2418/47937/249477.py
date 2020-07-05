a=int(input())
b=int(input())

#print(a)
#print(b)

if a%2!=0:
    print("[]")
else:
    x=int(a/2-b)
    if(x<0):
        print("[]")
    else:
        y=int(b-x)
        #print(x)
        #print(y)
        z=[]
        z.append(x)
        z.append(y)
        print(z)
        
   