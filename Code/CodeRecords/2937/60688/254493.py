a=list("CODEFESTIVAL2016");
b=list(input());
c=0;
for i in range(16):
    if(a[i]==b[i]):continue;
    else:c+=1;
print(c,end="")