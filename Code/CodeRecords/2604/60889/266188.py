letters = input().strip("[\"]").split("\", \"")
target = input()
answer = letters[0]
for letter in letters:
    if (letter>target>=answer) or (answer>letter>target) or (target>=answer>letter):
        answer = letter
print(answer)