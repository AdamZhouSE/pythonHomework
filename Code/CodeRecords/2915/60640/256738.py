n = int(input())
inp = [int(x) for x in input().split(" ")]
max_num = 1
curr_num = 1
for i in range(n-1):
    if inp[i] < inp[i + 1] <= 2*inp[i]:
        curr_num += 1
    else:
        if curr_num > max_num:
            max_num = curr_num
        curr_num = 1
print(max(max_num, curr_num))
