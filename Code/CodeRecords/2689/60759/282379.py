ts = int(input())
for t in range(ts):
    str1, str2 = input().split(' ')
    print(len(set(str1) | set(str2)))
