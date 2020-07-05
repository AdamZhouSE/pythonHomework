words = eval(input())
length_of_word = len(words[0])
pair = 0
for i in range(len(words)):
    for j in words[:i]+words[i+1:]:
        count = 0
        for k in range(length_of_word):
            if words[i][k] == j[k]:
                count = count + 1
            if count + 2 == length_of_word:
                pair = pair + 1
print(int(pair/2))