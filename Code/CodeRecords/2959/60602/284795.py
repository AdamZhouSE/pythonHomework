def subS(string, size):
    ans=[];
    if(size==1):
        i=0;
        while(i<len(string)):
            ans.append(string[i]);
            i+=1;
    else:
        delta=size;
        i=0;
        while(i+delta<=len(string)):
            ans.append(string[i:i+delta]);
            i+=1;
    return ans;



def findSameString(s1,s2):
    size=1;
    count=0;
    while(size<=len(s1)):
        ans1=subS(s1,size);
        ans2=subS(s2,size);
        i=0;
        while(i<len(ans1)):
            j=0;
            while(j<len(ans2)):
                if(ans1[i]==ans2[j]):
                    count+=1;
                j+=1;
            i+=1;
        size+=1;
    print(count);

s1=input();
s2=input();
findSameString(s1,s2);