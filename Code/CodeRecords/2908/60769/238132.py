num = int(input())
dict = []
for i in range(num):
    word = sorted(list(input()))
    if not word in dict:
        dict.append(word)
print(len(dict))