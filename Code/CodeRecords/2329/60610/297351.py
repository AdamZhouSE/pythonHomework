string=input();
string=string.replace("(","");
string=string.replace(")","");
string=list(map(int,string.split(",")));
if(1 in string):
    string.remove(1);
mid=[string[0]];
string.remove(string[0]);
result=0;
tar=0;
while(string!=[]):
    tar=0;
    length=len(string);
    i=0
    while(i<len(string)):
        cout=0;
        count=0
        for j in mid:
            for k in range(2,min(string[i],j)+1):
                if(string[i]%k==0)&(j%k==0):
                    mid.append(string[i]);
                    string.remove(string[i]);
                    count=1;
                    break;
            if(count==0):
                cout+=1;
            else:
                break;
        if(count==0):
            i+=1;
        if(cout==len(mid)):
            tar+=1;
    if (tar == length)|(string==[]):
        if (len(mid) > result):
            result = len(mid);
        if(string!=[]):
            mid = [string[0]];
            string.remove((string[0]));
if(len(mid)>result):
    reuslt=len(mid);
print(result)
