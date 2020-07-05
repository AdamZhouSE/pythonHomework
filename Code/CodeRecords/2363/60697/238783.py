a=str(bin(int(input())))
c=""
a=a[2:]
for i in range(len(a)):
    if(a[i]=="1"):
        c=c+"0"
    else:
        c=c+"1"
b=int(c,2)
print(b)
