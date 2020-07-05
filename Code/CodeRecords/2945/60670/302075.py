strr=input()
boy=0
girl=0
n=len(strr)
for i in range(0,n):
    if (strr[i]=='b') or ((i+1<n)and(strr[i+1]=='o')) or ((i+2<n)and(strr[i+2]=='y')):
        boy+=1
    if (strr[i]=='g') or ((i+1<n)and(strr[i+1]=='i')) or ((i+2<n)and(strr[i+2]=='r')) or ((i+3<n)and(strr[i+3]=='l')):
        girl+=1
print(boy)
print(girl,end='')