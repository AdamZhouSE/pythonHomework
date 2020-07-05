strings = eval(input())
stringA = strings[0].replace("a","1").replace("b", "1")
stringB = strings[1].replace("a","1").replace("b", "1")
stringFinal = stringA + " and " + stringB
if eval(stringFinal):
    print('true')
else:
    print('false')