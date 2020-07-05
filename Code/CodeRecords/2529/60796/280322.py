s=input()
ls=[]
for i in range(len(s)):
    ls.append(s[i])
#对于2的幂的正整数，有个规律：位数每隔3都有对应的整数个数4、3、3，
l=len(s)
n=l%3
if n==1:
    geshu=4
    min=int(l/3)*10
    max=min+3
elif n==2:
    geshu=3
    min=int(l/3)*10+4
    max=min+2
else:
    geshu=3
    min=int((l-1)/3)*10+7
    max=min+2

for i in range(min,max+1):
    s=str(pow(2,i))
    t=[]
    for j in range(len(s)):
        t.append(s[j])
    yes=True
    for j in range(len(t)):
        a=t[j]
        if not(ls.__contains__(a) and ls.count(a)==t.count(a)):
            yes=False
            break
    if yes:
        break

if yes:
    print("true")
else:
    print("false")

