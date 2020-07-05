a=int(input())
for i in range(a):
    b=int(input())
    c=bin(b)
    index=0
    val=0
    for j in range(len(c)):
        if c[j]=="1":
            index+=1
            val=j
    if index>1:
        print(-1)
    else:
        print(len(c)-int(val))