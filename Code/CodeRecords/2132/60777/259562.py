temp=input()

dic=['zero','one','two','three','four','five','six','seven','eight','nine']
num=[-1]*10
for i in range(10):
    con=True
    now=dic[i]
    for j in range(len(now)):
        if(not(now[j] in temp and temp.count(now[j])>=now.count(now[j]))):
            con=False
    if(con):
        temp=list(temp)
        for j in range(len(now)):
            temp.remove(now[j])
        temp=str(temp)
        num[i]=1
        
for i in range(10):
    if(num[i]==1):
        print(i,end='')
print()