# arr=eval(input())
arr=eval("[1,1,1,2,2,2]")
s=list(set(arr))
num=[]
for i in range(len(s)):
    t=arr.count(s[i])
    num.append(t)
print(s)
print(num)
begin=0
end=1
ans=[]
while(len(ans)!=len(arr)):
    while num[begin]*num[end]!=0:
        ans.append(s[begin])
        num[begin]-=1
        ans.append(s[end])
        num[end]-=1
    if num[begin]==0:
        begin=end+1
    if num[end]==0:
        end=begin+1
print(ans)