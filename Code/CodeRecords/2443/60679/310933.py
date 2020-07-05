from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        key = cmp_to_key(lambda a,b: int(b+a)-int(a+b))
        res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
        return res or '0'


t = Solution()
read = input()
read = read[1:len(read)-1]
arr = read.split(",")
arr = [int(arr[i]) for i in range(len(arr))]
print(t.largestNumber(arr))