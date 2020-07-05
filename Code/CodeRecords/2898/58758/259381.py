n = int(input())
bin_str = input()
if bin_str == '0':
    print('0')
else:
    count = 0
    for ch in bin_str:
        if ch == '0':
            count += 1
    ans = '1'
    for i in range(0, count):
        ans += '0'
    print(ans, end='')
