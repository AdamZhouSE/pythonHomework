numbers = int(input())
words = input().split(' ')
stairs = 0
out = []
for i in range(len(words)):
    num = 0
    if words[i] == '1':
        stairs += 1
    if words[i] == '1' and i != 0:
        out.append(words[i - 1])
out.append(words[numbers - 1])
out = ' '.join(out)
print(stairs)
print(out)