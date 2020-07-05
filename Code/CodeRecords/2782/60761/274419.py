n=int(input())
num=[]
minwave=[]
for i in range(n):
    b=int(input())
    fmin=10000000
    for j in num:
        fmin=min(fmin,abs(b-j))
    num.append(b)
    #print(minwave)
    if(not minwave):
        minwave.append(b)
    else:
        minwave.append(fmin)
print(sum(minwave),end="")