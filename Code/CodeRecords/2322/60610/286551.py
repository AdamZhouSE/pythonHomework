L=int(input());
R=int(input());
count=0;
for i in range(1,R+1):
    if(pow(i,2)>R):
        break;
    if(pow(i,2)>=L):
        string=str(i);
        Rstring=string[::-1];
        if(string==Rstring):
            n=pow(i,2);
            string=str(n);
            Rstring=string[::-1];
            if(string==Rstring):
                count+=1;
print(count);
