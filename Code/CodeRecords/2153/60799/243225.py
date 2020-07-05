s = input()
if '-' in s:
    print(s[0:s.index('-')+1] + s[:s.index('-'):-1])
else:
    print(s[::-1])