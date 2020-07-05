n,m=map(int,input().split(" "))
lis=[]
count=0
while(s=input()):
    if(s[0] not in lis and s[2] not in lis):
        lis.append(s[0])
        lis.append(s[2])
        count+=1;
print(count)