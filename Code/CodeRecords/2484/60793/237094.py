testNum = int(input())
set1s = []
set2s = []
for i in range(0, testNum):
    input()
    set1s.append(tuple(list(map(int, input().split(" ")))))
    set2s.append(tuple(list(map(int, input().split(" ")))))
for i in range(0, len(set1s)):
    set1 = set1s[i]
    set2 = set2s[i]
    result = len(set1 or set2)
    if result == 6:
        print(7)
        continue
    print(result)
