alphabet = [chr(i) for i in range(65,91)]
num = int(input())
answer = ""
for i in range(num):
    answer = answer +alphabet[i]
    j = len(answer)-2
    while j >= 0:
        answer = answer + answer[j]
        j = j - 1
print(answer)