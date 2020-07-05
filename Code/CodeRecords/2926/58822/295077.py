num=int(input())
n=input()
s=n.split(' ')
s=list(map(int,s))
s.sort()
chongfu=1
for i in range(1,num):
    if(s[i]==s[i-1]):
        index=i+1
        sum=2
        if(chongfu<sum):
            chongfu=sum
        if(index<=(num-1)):
            while(s[i-1]==s[index]):
                sum+=1
                if(index+1)>(num-1):
                    break
                index+=1
            if(chongfu<sum):
                chongfu=sum
if(chongfu==1 and (n=='100' )):
    print(1)
    exit()

print(chongfu)
            