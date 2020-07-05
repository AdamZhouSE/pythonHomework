num=input()
list=input().split()
ans=[]
for x in list:
    len_x=len(x)
    s=""+x[0]
    for i in range(len_x-1):
        if str(x[i])!=str(x[i+1]):
            s=s+x[i+1]
    ans.append(s)
print(" ".join(str(i) for i in ans))