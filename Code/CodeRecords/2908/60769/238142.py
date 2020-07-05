num = int(input())
dict = []
for i in range(num):
    word = sorted(list(input().strip()))
    if not word in dict:
        dict.append(word)
print(len(dict),end="")