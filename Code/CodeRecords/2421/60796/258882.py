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

