string = input()
K = int(input())
min_str = "z" * len(string)
for i in range(len(string) * 10):
    index = string.index(max(string[:K]))
    string = string[:index] + string[index+1:] + max(string[:K])
    if min_str > string:
        min_str = string
print(min_str)
