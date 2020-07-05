a=eval(input())
count=0
for i in range(1,a+1):
    ch=str(i)
    for i in range(0,len(ch)):
        if(ch[i]=='1'):count+=1
print(count)
