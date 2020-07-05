m,n=map(int,input().split(" "))
a=list(input())
b=list(input())
re=[]
for i in range(0,n):
    if a[0]=="*" or b[i]=="*" or a[0]==b[i]:
        for j in range(1,m):
            if not(a[j]=="*" or b[i+j]=="*" or a[j]==b[i+j]):
                break
        else:
            re.append(i+1)
re=[str(i) for i in re]
print(len(re))
print(" ".join(re),end=" \n")