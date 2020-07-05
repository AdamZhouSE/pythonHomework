#12
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
dup = []
for item in num:
    if item not in dup and item!=0:
        dup.append(item)
print(len(dup))