str1 = input()
str2 = input()


def generate(string):
    result = dict({})
    for i in range(1, len(string) + 1):
        for j in range(len(string) + 1 - i):
            if string[j:j+i] in result:
                result[string[j:j+i]] += 1
            else:
                result[string[j:j+i]] = 1
    return result


dict1 = generate(str1)
dict2 = generate(str2)
count = 0
for string1 in dict1:
    if string1 in dict2:
        count = count + dict1[string1]*dict2[string1]
print(count, end="")