a=str(input())
b=str(input())
count=0
for i in range(0,len(a)-len(b)+1):
    if a[i]==b[0]:
        judge=0
        for j in range(0,len(b)):
            if  not a[i+j]==b[j]:
                judge=1
                break
        if judge==0:
            count=count+1
print(count,end='')