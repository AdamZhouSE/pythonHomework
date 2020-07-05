A=eval(input())
dic2={}

def union(k, v):
    if k not in dic2:
        dic2[k] = k
    if v not in dic2:
        dic2[v] = v
    dic2[check(dic2[k])] = check(v)


def check(k):
    if dic2[k] != k:
        dic2[k] = check(dic2[k])
    return dic2[k]


# 由于最大10万，317 * 317已经超过最大值10万了，所以我们用这个上界，直接写死
prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
dic = {}
for v in A:
    new_v = v
    while new_v > 1:
        divide = new_v
        for c in prime_nums:
            if new_v % c == 0:
                divide = c
                break
            if c ** 2 > new_v + 10:
                break
        if divide not in dic:
            dic[divide] = []
        dic[divide].append(v)
        new_v = new_v / divide
for k in dic:
    dic[k] = list(set(dic[k]))

for nums in dic.values():
    k = nums[0]
    for v in nums:
        union(k, v)

counter = {}
for num in A:
    if num < 2:
        continue
    group_id = check(num)
    counter[group_id] = counter.get(group_id, 0) + 1

return max(counter.values())
