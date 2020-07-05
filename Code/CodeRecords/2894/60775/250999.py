len = int(input())
s = input()

idx = 0
last = 1
count = 0
while idx <= len-2:
    if (s[idx:idx+2] == 'KK' or s[idx:idx+2] == 'VV' )and last == 1:
        count += 1
        idx += 2
        last -= 1
    elif s[idx:idx+2] == 'VK':
        count += 1
        idx += 2
    else:
        idx += 1
print(count,end='')