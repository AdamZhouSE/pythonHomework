problems = int(input())
for p in range(problems):
    s = input().lower()
    
    judge = "YES"
    
    left = 0
    right = len(s)-1
    while left < right:
        if s[left]>'z' or s[left]<'a':
            left += 1
        elif s[right]>'z' or s[right]<'a':
            right -= 1
        else:
            if s[left] != s[right]:
                judge = "NO"
                break
            left += 1
            right -= 1
    print(judge)