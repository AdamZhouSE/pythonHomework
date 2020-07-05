num = bin(int(input()))[2:]
start = num.index('1')
ans = 0
count = 0
if start != -1:
    for i in range(start+1, len(num)):
        count += 1
        if num[i] == '1':
            if count > ans:
                ans = count
                count = 0
            else:
                count = 0
    print(ans)
else:
    print(ans)
