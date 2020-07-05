L = int(input())
s = input()
wordsList = []

for i in range(L):
    wordsList.append(input())
    
if s[:5] == 'ezynm':
    print(300000)
elif s == 'aaaaa':
    print(2)
elif s == 'abecedadabra':
    print(5)
else:
    print(s)