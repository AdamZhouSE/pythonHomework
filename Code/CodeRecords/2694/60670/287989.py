s=input()
n=len(s)
subs=''
finded=False
for k in range(n-1,0,-1):
    for i in range(0,n-k+1):
        astr=s[i:i+k]
        for j in range(i+1,n-k+1):
            bstr=s[j:j+k]
            if astr==bstr:
                subs=astr
                finded=True
                break
        if finded:
            break
    if finded:
        break
print(subs)