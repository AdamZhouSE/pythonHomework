n = int(input())
numbers = input()
numbers_s =numbers.split()
num_of_rank = []
counts = 1
for i in range(1,n):
    if numbers_s[i] == '1':
        num_of_rank.append(counts)
        counts = 1
    else:
        counts += 1
num_of_rank.append(counts)
print(str(len(num_of_rank)))
print(' '.join(str(w) for w in num_of_rank))
