n=int(input())
count=0
s=input().replace(" ","")
count=s.count("1")
s=s.split("1")
num=[]
for i in range(len(s)):
    num.append(len(s[i]))
p=num.index(max(num))
count = count + max(num)
a=1
if p!=0:
    while s[p-a]=='':
        count+=1
        if p-a!=0:
            a=a-1
        else: break
    if s[p+1]!='':
        count+=1
a=1
if p!=len(s)-1:
    while s[p+a]=='':
        count+=1
        if p+a!=len(s)-1:
            a=a+1
        else:break
    while s[p+a]=='':
        count+=1
        if p+a!=len(s)-1:
            a=a+1
        else:break
print(count-4)