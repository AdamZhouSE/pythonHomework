def lcp(first, second):
    index = 0
    while string[first] == string[second]:
        index += 1
        first += 1
        second += 1
        if second>=len(string)-1:
            break
    return index


nums = int(input())
string = input()
string_num = input().split(" ")
for i in range(nums):
    string_num[i] = int(string_num[i])
maximum = 0
for i in range(nums - 1):
    for j in range(i + 1, nums):
        length = lcp(i, j)
        if length + (string_num[i] ^ string_num[j]) > maximum:
            maximum = string_num[i] ^ string_num[j] + length
print(maximum)
