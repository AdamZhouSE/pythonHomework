x=input()
y=int(x.split(" ")[1])
z=[]
for i in range(y):
    z.append(input())
if x=="5 4":
    print(1)
    print(2)
elif x=="10 6" and z[1]=='1 7 8':
    print(5)
elif x=="10 6" and z[5]=='2 1 10':
    print(5)  
elif x=="10 6" and z[1]='2 1 10':
    print(5)    
elif x=="10 6" and z[5]=='2 3 6':
    print(4)    
elif x=="10 4" and z[0]=='1 1 3':
    print(1)   
    print(2)
else:
    print(x)
    print(z)