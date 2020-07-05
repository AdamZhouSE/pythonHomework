
def to_int_list(l, split):
    l = l.split(split)
    l = all_to_int(l)
    return l


def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


num = int(input())
nums = to_int_list(input(), " ")
t = 0
for i in nums:
    t += i
nums.sort(reverse=True)
big = nums[0]
if t % 2 == 0 and big <= t//2:
    print("YES")
else:
    print("NO")