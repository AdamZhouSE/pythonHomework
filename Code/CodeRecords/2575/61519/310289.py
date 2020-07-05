string=list(input())
res=[0]*len(string)
for i in range(1,len(string)):
    if string[i]==string[i-1]:
        res[i]=1-res[i-1]
    else:
        res[i]=res[i-1]
print(res)