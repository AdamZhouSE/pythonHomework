num=list(input())
num=[int(i) for i in num]
re=[]
while not list(set(num))==[0]:
    n=max(num)
    for i in num:
        if i>0 and i<n:
            n=i
    temp=[]
    for i in range(0,len(num)):
        if num[i]==0:
            temp.append(0)
        else:
            num[i]=num[i]-n
            temp.append(1)
    temp=[str(i) for i in temp]
    for i in range(0,n):
        re.append(int("".join(temp)))
print(len(re))
print(" ".join(re))