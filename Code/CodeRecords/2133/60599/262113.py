s=list(map(int,input().split(',')))
minN=min(s)
sum=0
for i in range(len(s)):
    s[i] = s[i]-minN
for i in s:
    sum+=i
print(sum)