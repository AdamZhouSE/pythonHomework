n = int(input())
for i in range(0, n):
    stack = []
    string = input().replace(" ", "")
    muti = 1
    pre = ""
    couple = []
    outcomeString = ""
    for i in string:
        if i.isdigit():
            muti = int(i)
            continue
        elif i.isalpha():
            outcomeString = outcomeString + i
            continue
        elif i == "[":
            couple.append(muti)
            couple.append(outcomeString)
            stack.append(couple)
            couple = []
            muti = 1
            outcomeString = ""
            continue
        elif i == ']':
            outcomeString = stack[-1][1] + stack[-1][0] * outcomeString
            del stack[-1]
    print(outcomeString)