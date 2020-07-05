s=input()
#print(s)
boy=0
girl=0
l=len(s)
for i in range(l):
    if s[i]=='b' or (i+1<l and s[i+1]=='o') or (i+2<l and s[i+2]=='y'):
        boy+=1
        
    elif s[i]=='g' or (i+1<l and s[i+1]=='i') or (i+2<l and s[i+2]=='r') or (i+3<l and s[i+3]=='l'):
        girl+=1
        
print(boy)
print(girl)
 