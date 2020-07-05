import re
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = int(input())
left = 0
right = 0
for i in range(0, len(s)):
    right += s[i]
    if left < s[i]:
        left = s[i]
ans = right
while left <= right:
    mid = (left+right)>>1;
    sum = 0
    cnt = 1
    for i in range(0, len(s)):
        if sum+s[i]>mid:
            cnt += 1
            sum = s[i]
        else:
            sum += s[i]
    if cnt <= n:
        ans = min(ans, mid)
        right = mid-1
    else:
        left = mid+1
print(ans)