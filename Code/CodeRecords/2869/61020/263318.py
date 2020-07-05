n = int(input())
nums = input().split()

for j in range(0, n):
    nums[j] = int(nums[j])

result_list = []
i = n - 1
while i >= 0:
    if nums[i] not in result_list:
        result_list.insert(0, nums[i])

    i -= 1

print(len(result_list))

# result_str = " ".join(result_list)
# print(result_str)

result_str = ""
for num in result_list:
    result_str += (num + " ")

print(result_str)
# k = 0
# while k < len(result):
#     print(result[k], end=" ")
#     if k != len(result) - 1:
#         print(" ", end="")
#
#     k += 1
