s = input()
s1 = ""
for i in range(len(s)):
    if s[i] != "[" and s[i] != "]":
        s1 += s[i]
array = s1.split(",")
array = [int(x) for x in array]
array.sort()
print(array)
