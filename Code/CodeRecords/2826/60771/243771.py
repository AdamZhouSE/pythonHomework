#32
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
dup = []
count = 0
while len(dup) != n:
    for item in num:
        while item in dup:
            item += 1
            count += 1
        else:
            dup.append(item)
print(count)