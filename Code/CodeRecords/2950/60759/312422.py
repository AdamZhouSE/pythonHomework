string = input()
if len(string) % 2 or string.count('2') != string.count('5'):
    print(-1)
else:
    vis = [False for i in range(len(string))]
    ans = 0
    record = 0
    for i in range(len(string)):
        record += 1 if string[i] == '2' else -1
        ans = max(ans, abs(record))
        if string[i] == '2':
            for j in range(i + 1, len(string)):
                if string[j] == '5' and not vis[j]:
                    vis[j] = True
                    break
            else:
                print(-1)
                break
    else:
        print(ans)
