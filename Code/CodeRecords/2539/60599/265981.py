s=list(eval(input()))
k=s.copy()
k.sort()
begin=-1
end=-1
for i in range(len(s)):
    if(s[i]!=k[i] and begin==-1):
        begin=i
    if(s[i]!=k[i]):
        end=i
print(end-begin+1)
