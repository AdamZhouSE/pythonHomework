x=input()
lis=list(x)
ans=""
for i in range(0,len(x)):
    if lis[i]=="6":
        ans=ans+"9"+x[i+1:]
        break
    else:
        ans=ans+lis[i]
print(ans)