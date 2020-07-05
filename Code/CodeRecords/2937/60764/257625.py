s=input()
standard="CODEFESTIVAL2016"
res=0
for i in range(len(standard)):
    if s[i]!=standard[i]:
        res+=1
print(res)