num=int(input())
s=input()
n=s.split(' ')
flag=0
index=0#0 kongjian  1 jianshen     2 biancheng 3 random
sum=0
for i in range(0,len(n)):
    if(n[i]=='0'):
        flag=0
        continue
    if(n[i]=='3'):
        sum+=1
        if(flag==0):
            flag=3
        else:
            if(flag==1):
                flag=2
            else:
                if(flag==2):
                    flag=1
        continue
    if(flag==0 or flag==3):
        if (n[i] == '1'):
            sum += 1
            flag = 2
        else:
            if(n[i]=='2'):
                sum+=1
                flag=1
        continue
    if(flag==1):
        if(n[i]=='1'):
            sum+=1
            flag=2
        else:
            flag=0
        continue
    if(flag==2):
        if(n[i]=='2'):
            sum+=1
            flag=1
        else:
            flag=0
        continue
print(num-sum)