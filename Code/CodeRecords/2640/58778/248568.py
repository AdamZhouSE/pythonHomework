s=input()
target=input()
re=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        x=0
        temp=s[i:j]
        for c in target:
            if(temp.count(c)==0):
                x=1
                break
        if(x==0):
            re.append(temp)
            break
count=[]
if(len(re)==0):
    print("")
else:
    for i in re:
        count.append(len(i))
    x=min(count)
    print(re[count.index(x)])