input()
nums = list(map(int,input().split(" ")))
# nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
count = 0
dict = {1:0,2:0,3:0,4:0}
for num in nums:
    dict[num] += 1
count += dict[4]
count += dict[3]
if(dict[3] <= dict[1]):
    dict[1] -= dict[3]
    number = dict[1] * 1 + dict[2] * 2
    if(number % 4 != 0):
        count += int(number/4) + 1
    else:
        count += int(number/4)
else:
    if (dict[2] % 2 != 0):
        count += int(dict[2] / 2) + 1
    else:
        count += int(dict[2] / 2)
print(count)