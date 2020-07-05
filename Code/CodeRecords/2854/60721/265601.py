lis=input().split(" ")
lis=[int(i) for i in lis]
lis.sort()
n=1
a=lis[0]
for x in lis:
    if(a!=x):
        n=n+1
        a=x
if(n==2):
    if lis.count(lis[5])==2 or lis.count(lis[5])==4:
        print("Elephant")
    elif lis.count(lis[5])==5:
        print("Bear")
    else:
        print("Alien")
elif(n==1):
    print("Elephant")
elif(n==3):
    if lis.count(lis[0])==4 or lis.count(lis[5])==4 or lis.count(lis[1])==4:
        if lis.count(lis[0])!=2 and lis.count(lis[2])!=2 and lis.count(lis[4])!=2:
            print("Bear")
        else:
            print("Alien")           
    else:
        print("Alien")        
else:
    print("Alien")
    
    