s = input()
ral = 0
dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
size = len(s)
for i in range(size):
    res = dict1[s[i]]
    if i == size - 1 or dict1[s[i + 1]] <= dict1[s[i]]:
        ral += res
    else:
        ral -= res
print(str(ral))