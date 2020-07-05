a=eval(input())
b=[]
for i in range(len(a)-1,-1,-1):
    if i<len(a)-1:
        temp=0
        if a[i]<a[i+1]:
            total=0
            for j in range(i+1,len(a)):
                if a[i]>a[j]:
                    total+=1
            b.insert(0,total)
        elif a[i]==a[i+1]:
            b.insert(0,b[0])
        else:
            b.insert(0,b[0]+1)

    else:
        b.append(0)
print(b)