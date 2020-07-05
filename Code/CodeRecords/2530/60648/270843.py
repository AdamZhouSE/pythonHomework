s1=input()
s2=input()
ls=[]
for i in s2:
    count=0
    for j in s1:
        if i!=j:
            count+=1
    if count==len(s1):
        ls.append(i)
s=""
for i in ls:
    s+=i
print(s1+s)