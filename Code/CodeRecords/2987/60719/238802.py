s = input()
size = len(s)
while size > 0:
    s = s + s[size-1]
    size = size - 1
print(s)
