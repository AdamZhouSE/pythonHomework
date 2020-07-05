n=int(input())
arr=list(map(int,input().split()))
begin=0
end=0
count=[]
while(end!=len(arr)):
    while end!=len(arr) and arr[end]==arr[begin]:
        end+=1
    count.append(end-begin)
    begin=end
ans=[]
for i in range(len(count)-1):
    ans.append(min(count[i],count[i+1]))
ans.sort()
print(ans[-1]*2)