string=input();
i=len(string)-1;
count=0;
while(i!=0):
    for j in range(len(string)):
        if(j+i<len(string)):
            if(string[j:j+i] in string[j+1:]):
                print(string[j:j+i]);
                count=1;
                break;
    if(count==1):
        break;
    i-=1
if(count==0):
    print("")
    