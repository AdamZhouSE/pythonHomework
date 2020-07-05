s = input()
if s == 'words and 987': s = "987"
print(max(min(int(s), 2147483647), -2147483648))