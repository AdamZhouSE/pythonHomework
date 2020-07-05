from collections import Counter
nums=eval('['+input()+']')
c=Counter(nums)
print(c.most_common(1)[0][0])