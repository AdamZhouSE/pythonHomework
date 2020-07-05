length = int(input())
string = list(input())
index = 0
count = 0
while index < len(string) - 1:
    if string[index] == string[index + 1]:
        del string[index]
        index -= 1
        count += 1
    index += 1
print(count)