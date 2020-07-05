n_m=input().split()
s1=list(input())
s2=list(input())
count=0
res=[]
if(len(s2)>=len(s1)):
    for i in range(len(s2)-len(s1)+1):
        a=s2[i:i+len(s1)]
        for j in range(len(s1)):
            if(s1[j]=="*"):
                a[j]="*"
        b=s1.copy()
        for j in range(len(a)):
            if(a[j]=="*"):
                b[j]="*"
        if(a==b):
            count=count+1
            res.append(i+1)
print(count)
print(*res)