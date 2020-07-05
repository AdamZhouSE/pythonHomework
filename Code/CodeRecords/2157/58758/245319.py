roma = input() + '0'
ans = 0
for i in range(0, len(roma)-1):
    if roma[i] == 'M':
        ans += 1000
    elif roma[i] == 'D':
        ans += 500
    elif roma[i] == 'C':
        if roma[i+1] == 'D' or roma[i+1] == 'M':
            ans -= 100
        else:
            ans += 100
    elif roma[i] == 'L':
        ans += 50
    elif roma[i] == 'X':
        if roma[i+1] == 'L' or roma[i+1] == 'C':
            ans -= 10
        else:
            ans += 10
    elif roma[i] == 'V':
        ans += 5
    else:
        if roma[i+1] == 'V' or roma[i+1] == 'X':
            ans -= 1
        else:
            ans += 1
print(ans)
