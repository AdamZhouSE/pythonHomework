s=input()
dif=int(input())
small=int(input())
large=int(input())
res=0

for i in range(len(s)):
    for j in range(i+small,len(s)):
        if(j>i+large):
            break
        pre=s[i:j]
        d=[]
        temp=0
        for k in range(len(pre)):
            if(pre[k] not in d):
                d.append(pre[k])
        num=len(d)
        if(num>dif):
            continue
        for k in range(len(s)-len(pre)+1):
            if(s[k:k+len(pre)]==pre):
                temp+=1
        if(temp>res):
            res=temp
print(res)