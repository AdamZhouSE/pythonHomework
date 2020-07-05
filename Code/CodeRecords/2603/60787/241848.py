a=input()
a=a[1:len(a)-1]
num=a.split(",")
num=[int(i) for i in num]
k=int(input())
re=[]
for i in range(0,len(num)-1):
    for j in range(i+1,len(num)):
        re.append(abs(num[i]-num[j]))
re=sorted(re)
print(re[k-1])