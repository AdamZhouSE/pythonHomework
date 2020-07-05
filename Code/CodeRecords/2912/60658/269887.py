arr = input()
l = 0
r = 0
n = len(arr)
s = set()
ans = 0
while r<n:
    if arr[r] in s:
        s.remove(arr[l])
        l+=1
    else:
        s.add(arr[r])
        r+=1
        ans = max(ans,len(s))
print(ans)