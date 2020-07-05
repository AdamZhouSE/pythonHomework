string = input()
dict1 = {"zero": "z", "two": "w", "four": "u", "six": "x", "eight": "g"}
dict2 = {"one": "o", "three": "r", "five": "f", "seven": "s", "nine": "e"}
record = {}
for i in range(0, len(dict1.values())):
    key = list(dict1.keys())[i]
    value = list(dict1.values())[i]
    temp = string.count(value)
    if temp != 0:
        record[key] = temp
        for char in key:
            index = string.index(char)
            string = string[0:index] + string[index + 1:]

for i in range(0, len(dict2.values())):
    key = list(dict2.keys())[i]
    value = list(dict2.values())[i]
    temp = string.count(value)
    if temp != 0:
        record[key] = temp
        for char in key:
            index = string.index(char)
            string = string[0:index] + string[index + 1:]

num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
result = ""
for i in range(0, 10):
    word = num[i]
    time = record.get(word)
    if time != None:
        for j in range(0, time):
            result += str(i)

print(result)
