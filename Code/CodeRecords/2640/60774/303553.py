s = input()
target = list(input())
minStr = s + ' '
for i in range(0,len(s)):
    for j in range(i + 1,len(s) + 1):
        temp = list(s[i:j])
        cmp = [ch for ch in target if ch in temp]
        if(cmp == target):
            qualified = s[i:j]
            if(len(qualified) < len(minStr)):
                minStr = qualified
if(minStr == s + ' '):
    print('')
else:
    print(minStr)