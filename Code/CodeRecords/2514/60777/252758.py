s=input()
t=input()
res=True
for i in range(len(s)):
    find=False
    for j in range(len(t)):
        if(s[i]==t[j]):
            i+=1
            j+=1
            find=True
    if(find==False):
        res=False

print(res)
