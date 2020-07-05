l=eval('['+input().replace(' ',',')+']')
n=l[0];m=l[1]
sum=0
result=0
s=[]
for i in range(n):
    s.append(eval('['+input().replace(' ',',')+']'))
    sum+=s[i][0]
s=sorted(s,key=lambda x:x[0]-x[1],reverse=True)
for i in s:
    if sum>m:
        sum-=i[0]-i[1]
        result+=1
    else:
        break
if sum>m:
    result=-1
print(result)