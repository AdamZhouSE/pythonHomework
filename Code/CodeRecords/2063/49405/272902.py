s = input()
print(s[:len(s) // 2] == reversed(s)[:len(s) // 2])