s=input()
#print(s)
boy=0
girl=0
l=len(s)
for i in range(l):
    if s[i]=='b' or (s[i+1]=='o' and i+1<l) or (s[i+2]=='y' and  i+2<l):
        boy+=1
    elif s[i]=='g' or (s[i+1]=='i' and i+1<l) or (s[i+2]=='r' and i+2<l) or (s[i+3]=='l' and i+3<l):
        girl+=1
print(boy)
print(girl)
 