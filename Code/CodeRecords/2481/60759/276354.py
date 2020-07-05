ts = int(input())
for t in range(ts):
    input()
    set1, set2 = set(input().split(' ')), set(input().split(' '))
    print(len(set1 & set2))
