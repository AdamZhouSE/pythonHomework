s=input()
t=input()
t=t[2:len(t)-2]
ls=[]
ls=t.split("]")
for i in range(len(ls)):
    if i>0:
        ls[i]=ls[i][2:]
        ls[i]=ls[i].split(",")
        for j in range(len(ls[i])):
            ls[i][j]=int(ls[i][j])
n=[]
for i in range(len(s)):
    n.append(s[i])
for p in range(len(ls)):
    for i in range(len(n)-1):
        j=i+1
        while j<=len(n)-1:
            before=ord(n[i])
            after=ord(n[j])
            if after<before:
                substring1=str(i)+","+str(j)
                substring2=str(j)+","+str(i)
                if t.__contains__(substring1) or t.__contains__(substring2):
                    temp=n[i]
                    n[i]=n[j]
                    n[j]=temp
            j=j+1
result=""
for i in range(len(n)):
    result=result+n[i]
print(result)