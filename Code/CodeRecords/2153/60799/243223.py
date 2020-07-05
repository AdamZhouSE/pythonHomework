s = input()
if '-' in s:
    s = (s[0:s.index('-')+1] + s[:s.index('-'):-1])
print(s[::-1])