def rotate(string):
    string = string[1:] + string[0]
    return string




rawString = input()
stringArrays = []
for i in range(len(rawString)):
    rawString = rotate(rawString)
    stringArrays.append(rawString)
stringArrays.sort()
outcome = ""
for i in stringArrays:
    outcome += i[-1]
print(outcome,end="")