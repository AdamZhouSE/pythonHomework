n = int(input())
current_str = ''
for i in range(n):
    current_str = str(current_str) + chr(ord('A') + i) + str(current_str)
print(current_str)