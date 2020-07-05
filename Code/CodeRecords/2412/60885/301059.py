def count_less(nums, target):
    count = 0
    for num in nums:
        if num != 0 and num < target:
            count += 1
    return count

def cycle_sort(nums, s, first):
    q = 0
    idss = []
    found = set()
    while len(found) < len(nums):
        while first in found:
            first = (first + 1) % len(nums)
        carry = nums[first]
        nums[first] = 0
        ids = []
        while carry != 0:
            count = count_less(nums, carry)
            while nums[count] == carry:
                count += 1
            carry,nums[count] = nums[count],carry
            ids.append(count)
        if len(ids) > 1 and len(ids) > s:
            return -1,[]
        found = found.union(set(ids))
        if len(ids) > 1:
            idss.append(ids)
            q += 1
    return q,idss

def find_min(n,s,nums):
    ans_q = -1
    ans_idss = []
    for i in range(n):
        q,idss = cycle_sort(nums.copy(), s, i)
        if q != -1 and (ans_q == -1 or q < ans_q):
            ans_q = q
            ans_idss = idss
    return ans_q, idss

n,s = list(map(int, input().split()))
nums = list(map(int, input().split()))
q,idss = find_min(n,s,nums)
if q == 2:
    q = -1
print(q)
if q != -1:
    for ids in idss:
        print(len(ids))
        for num in ids:
            print(num+1, end=' ')
        print()