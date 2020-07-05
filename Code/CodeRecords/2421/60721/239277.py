x=list(input())
for i in range(0,len(x)):
    if(x[i]=='6'):
        x[i]='9'
        break
for m in x:
    print(m,end="")
print()