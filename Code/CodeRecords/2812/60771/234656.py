#3
n = int(input())
l = input().split(" ")
duplicate = []
for item in l:
    if item not in duplicate:
        if item != '0':
            duplicate.append(item)
print(len(duplicate))