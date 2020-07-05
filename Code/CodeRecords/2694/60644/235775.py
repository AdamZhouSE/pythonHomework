str=input()
l=0
res=""
for i in range(0,len(str)):
    for j in range(i+1,len(str)+1):
        for k in range(0,len(str)+i-j):
            if str[k:k+j-i]==str[i:j] and k!=i:
                if j-i>l:
                    l=j-i
                    res=str[i:j]
                break
print(res)

