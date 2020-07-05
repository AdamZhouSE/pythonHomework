snums = input()
snums = snums.replace('[','')
snums = snums.replace(']','')
snums = snums.split(',')
longest_streak = 0
size = len(snums)
for i in range(0,size):
    snums[i] = int(snums[i])
num_set = set(snums)
for num in num_set:
    if num - 1 not in num_set:
        current_num = num
        current_streak = 1
        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1
        longest_streak = max(longest_streak, current_streak)
print(longest_streak)