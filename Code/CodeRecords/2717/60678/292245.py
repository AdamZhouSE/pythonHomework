strings = eval(input())
stringA = list(strings[0])
stringB = list(strings[1])
for i in range(len(stringA)):
    if str(stringA[i]).isalpha():
        stringA[i] = "1"
    if str(stringB[i]).isalpha():
        stringB[i] = '1'
stringFinal = ''.join(stringA) + " and " + ''.join(stringB)
if eval(stringFinal):
    print('true')
else:
    print('false')