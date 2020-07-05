n = input()
key = list(set(list(map(int, input().split(' ')))))
print(len(key) - key.count(0))