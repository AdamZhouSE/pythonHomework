def maxProduct(words):
     return max([len(w1) * len(w2) for w1 in words for w2 in words if not set(w1) & set(w2)] or [0])


words = input()
print(maxProduct(words))