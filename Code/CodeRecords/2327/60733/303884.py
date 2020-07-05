s=input()
lo, hi = 0, len(s)
ans = []
for x in s:
    if x == 'I':
        ans.append(lo)
        lo += 1
    else:
        ans.append(hi)
        hi -= 1
print(ans+[lo])