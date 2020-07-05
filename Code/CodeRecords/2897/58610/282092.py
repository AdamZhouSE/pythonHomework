words = eval(input())

def no_common(word_a: str, word_b: str):
    return len(set(word_a) & set(word_b)) == 0

res = 0
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if no_common(words[i], words[j]):
            res = max(res, len(words[i]) * len(words[j]))
print(res)