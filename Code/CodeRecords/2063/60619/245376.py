string = input()
rString = list(string)
rString.reverse()
rString = ''.join(rString)
if int(string) == int(rString):
    print(True)
else:
    print(False)
