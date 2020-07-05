n=int(input())
max=n
l=str(n)

for i in range(len(l)):
    if l[i]!="6" and l[i]!="9":
        break
    if l[i]=="6":
        a="9"
    else:
        a="6"
    t=l[:i]+a+l[i+1:]
    if int(t)>max:
        max=int(t)
print(max)
#注意：如果有别的不是6或9的数字，那就返回原数

