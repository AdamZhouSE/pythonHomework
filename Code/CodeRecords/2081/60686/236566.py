string_f = input()
string_c = input()
count = 0
for i in range(0, len(string_f) - len(string_c) + 1):
    if string_f[i] == string_c[0]:
        if string_f[i:i + len(string_c)] == string_c:
            count += 1
print(count, end="")
