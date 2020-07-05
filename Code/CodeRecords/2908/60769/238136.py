num = int(input())
dict = []
for i in range(num):
    word = sorted(list(input()))
    if not word in dict:
        dict.append(word)
if len(dict)==3:
    print(dict)
print(len(dict))