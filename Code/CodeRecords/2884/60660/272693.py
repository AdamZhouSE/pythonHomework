t=eval('['+input().replace(' ',',')+']')
k=t[1];n=t[0]
l=eval('['+input().replace(' ',',')+']')
sum=0
for i in range(n):
    for j in range(n):
        if i!=j and abs(l[i]-l[j])<=k:
            sum+=1
print(sum)