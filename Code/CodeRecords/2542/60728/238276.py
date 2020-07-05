

def format(s):
    leng = len(s)
    for i in range(0, leng):
        s[i] = int(s[i])

    return s


def longestConsecutive(nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best

a=input()
a=list(a)
a[0]=''
a[len(a)-1]=''
s=''.join(a)
m=s.split(",")
m=format(m)
print (longestConsecutive(m))