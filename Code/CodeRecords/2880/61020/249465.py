# import os
# import sys

s = input()
n_k_list = s.split()

n = int(n_k_list[0])
k = int(n_k_list[1])

'''
8 4
4 2 3 1 5 1 6 4'''

weight_list = input().split()

for i in range(0, len(weight_list)):
    weight_list[i] = int(weight_list[i])

left_index = 0
while (left_index < len(weight_list)) and (weight_list[left_index] <= k):
    left_index += 1

if left_index == len(weight_list):
    print(n)
    # os._exit()
#    sys.exit(0)

else:
    right_index = len(weight_list) - 1
    while weight_list[right_index] <= k:
        right_index -= 1

    print(n - (right_index - left_index + 1))
