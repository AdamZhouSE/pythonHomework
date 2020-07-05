# n = int(input())
lines = []

for i in range(1, n + 1, 2):
    num_of_stars = (n - i) // 2
    line = '*' * num_of_stars + 'D' + '*' * num_of_stars
    lines.append(line)

lines_to_be_rev = lines[:-1]
lines_to_be_rev.reverse()
lines += lines_to_be_rev

for _line in lines:
    print(_line)

# test
# nums = [1, 2, 3, 4, 5, 6, 7]
# a = nums[2:5]
# a.reverse()
# print(nums)
