n=int(input())
sum=0
result=0
s=[]
for i in range(n):
    s.append(eval('['+input().replace(' ',',')+']'))
s.insert(0,[-99999,0])
s.append([99999,0])
for i in range(1,n+1):
    if s[i][0]-s[i][1]>s[i-1][0]:
        result+=1
        continue
    if s[i][0]+s[i][1]<s[i+1][0]:
        result+=1
        s[i][0]+=s[i][1]
print(result)