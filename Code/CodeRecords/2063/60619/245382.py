string = input()
result = True
i = 0
j = len(string)-1
while i < j:
    if string[i] != string[j]:
        result = False
        break
    i += 1
    j -= 1
print(result)
