n=input()
boy=0
girl=0
k=len(n)
for i in range(0,len(n)):
    if(n[i]=='b') or(i+1<k and n[i+1]=='o')or(i+2<k and n[i+2]=='y'):
        boy+=1
    if(n[i]=='g' ) or(i+1<k and n[i+1]=='i' ) or(i+2<k and n[i+2]=='r') or(i+3<k and n[i+3]=='l'):
        girl+=1
    i+=1
print(boy)
print(girl,end='')