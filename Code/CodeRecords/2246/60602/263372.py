import itertools
def judge(num):
    num = int(num)
    return True if num == 0 or num & (num - 1) == 0 else False
Judge=False;
temp=input();
for x in itertools.permutations(temp,len(temp)):
    if(x[0]=='0'):
        continue;
    else:
        ans="";
        i=0;
        while(i<len(x)):
            ans+=str(x[i]);
            i+=1;
        ans=int(ans);
        if(judge(ans)):
            Judge=True;
print(Judge);