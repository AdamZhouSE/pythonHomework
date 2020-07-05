row=eval(input())
n=len(row)//2
count=0
for i in range(0,n):
    t=2*i
    if row[t]%2==0:
        if row[t]+1!=row[t+1]:
            for j in range(t+2,2*n):
                if row[t]+1==row[j]:
                    row[j]=row[t]
                    row[t]+=1
                    count=j-i-1
                    break
    elif row[t]%2==1:
        if row[t]-1!=row[t+1]:
            for j in range(t+2,2*n):
                if row[t]-1==row[j]:
                    row[j]=row[t]
                    row[t]-=1
                    count=j-i-1
                    break
print(count)