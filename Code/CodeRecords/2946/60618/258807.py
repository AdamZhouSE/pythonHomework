a=list(input())
count=0
for i in range(len(a)-1,-1,-1):
    if a[i]=='0':
        count+=1
        for j in range(0,i):
            if a[j]=='1':
                a[j]='0'
            else:
                a[j]='1'
print(count)