a=list(input())
b=sorted(a)
num=[]
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[len(a)-j-1] and (len(a)-j) not in num:
            num.append(len(a)-j)
for i in range(len(a)-1):
    print(num[i],end=" ")
print(num[len(a)-1])