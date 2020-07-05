arr = [int(i) for i in input()[1:-1].split(',')]
lower = int(input())
upper = int(input())
sub_arrs = [arr[i:j] for i in range(0, len(arr)) for j in range(i+1, len(arr) + 1)]
count = 0
for each in sub_arrs:
    if lower <= sum(each) <= upper:
        count += 1
print(count)
