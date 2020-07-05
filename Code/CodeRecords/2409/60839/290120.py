x=input()
lis=list(map(int,x.split(",")))

odd=[]
even=[]

for i in lis:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

temp=[] #存放差值
for i in odd:
    for j in even:
        temp.append(abs(i-j))
m=min(temp)
print(m*(len(odd) if len(odd)<len(even) else len(even)))