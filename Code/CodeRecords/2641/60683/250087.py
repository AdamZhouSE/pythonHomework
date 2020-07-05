s1 = input().strip()
s2 = input().strip()
print(s1 in s2 or s1[::-1] in s2)