s=list(eval(input()))
res=[]
for i in range(len(s)):
    count = 0
    for k in range(i+1,len(s)):
        if(s[i]>s[k]):count+=1
    res.append(count)
print(res)