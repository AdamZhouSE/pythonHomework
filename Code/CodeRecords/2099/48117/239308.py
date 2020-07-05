excel = input()
para = len(excel) - 1
answer = 0

for word in excel:
    answer += ((ord(word) - 64) * pow(26, para))
    para -= 1
print(answer)