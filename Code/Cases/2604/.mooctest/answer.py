import ast
letters = ast.literal_eval(input())
target = input()

letters.append(target)
letters.sort()
index = 0
for i in range(letters.__len__()):
    if letters[letters.__len__()-1-i] == target:
        index = letters.__len__()-1-i
        break
if index == letters.__len__()-1:
    print(letters[0])
else:
    print(letters[index+1])