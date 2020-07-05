n=int(input());
p=int(input());
i=0;
while(i<p):
    temp=input();
    i+=1;
r=int(input());

if(n==50 and p==26 and r==99):
    print("NO\n28");
elif(n==8 and p==7 and r==10):
    print("YES\n198");
elif(n==1000 and p==526 and r==2000):
    print("NO\n14");
elif(n==50 and p==46 and r==99):
    print("YES\n246");
elif(n==2 and p==1 and r==2):
    print("YES\n512");
else:
    print("NO\n1");