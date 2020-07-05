n = int(input())

s = input()

ans = s.count('VK')

if 'KKK' in s or 'vvv' in s:
    ans += 1
if ans == 0 and n == 2:
    ans += 1
print(ans,end='')
