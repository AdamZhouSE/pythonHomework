import collections
str1=input()
str2=input()
c1=collections.Counter(str1)
c2=collections.Counter()
l=r=0
sig=0
while r<len(str2):
    c2[str2[r]]+=1
    if(c1==c2):
        sig=1
        print("True")
        break;
    r+=1;
    if r-l+1>len(str1):
        c2[str2[l]]-=1
        if c2[str2[l]]==0:
            del c2[str2[l]];
        l+=1;
if(sig==0):
    print("False")