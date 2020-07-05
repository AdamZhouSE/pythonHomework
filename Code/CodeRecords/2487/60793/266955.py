from collections import Counter
for test in range(0, int(input())):
    input()
    names = Counter(list(input().split()))
    sorted(names.items(), key=lambda item:item[1], reverse=True)
    a = names.pop(0)
    print(a[0], a[1])