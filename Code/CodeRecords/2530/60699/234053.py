strA=input()
strB=input()
dict={}
for i in strB:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
res=""
for i in strA:
    if i in dict:
        res+=i*dict[i]
        dict[i]=0
for i in dict:
    if dict[i]!=0:
        res+=i*dict[i];
print(res)