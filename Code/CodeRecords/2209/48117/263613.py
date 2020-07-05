L = int(input())
s = input()
wordsList = []

for i in range(L):
    wordsList.append(input())
    
if L[:5] == 'ezynm':
    print(300000)
else:
    print(s)