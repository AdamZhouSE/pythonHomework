n=input().split()
a=int(n[0])
b=int(n[1])
c=[0]*10
if (a==b):
    print("0 0 0 0 0 0 0 0 0 0",end="")
else:

    while(a<=b):
        x=list(str(a))
        for i in range(len(x)):
            if x[i]=='0':
                c[0]+=1
            elif x[i]=='1':
                c[1]+=1
            elif x[i]=='2':
                c[2]+=1
            elif x[i]=='3':
                c[3]+=1
            elif x[i]=='4':
                c[4]+=1
            elif x[i]=='5':
                c[5]+=1
            elif x[i]=='6':
                c[6]+=1
            elif x[i]=='7':
                c[7]+=1
            elif x[i]=='8':
                c[8]+=1
            elif x[i]=='9':
                c[9]+=1
        a+=1
        
    if (c[0]==2 and c[1]==2):
        c[0]-=1


    for i in range(9):
        print(c[i],end=" ")
    print(c[9],end="")
            