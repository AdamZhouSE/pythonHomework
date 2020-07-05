a=list(input())
b=sorted(a)
num=[]
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j] and (1+j) not in num:
            num.append(1+j)
for i in range(len(a)-1):
    print(num[i],end=" ")
print(num[len(a)-1])