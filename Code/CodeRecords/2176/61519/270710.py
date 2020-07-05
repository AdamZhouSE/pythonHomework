a=list(input())
b=sorted(a)
num=[]
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[len(a)-1-j] and (len(a)-j) not in num:
            num.append(len(a)-j)
for i in range(len(a)):
    print(num[i],end=" ")