def solution(inputString):
    if inputString.isdigit():
        return [int(inputString)]
    result = []
    for i, char in enumerate(inputString):
        if char in ["+", "-", "*"]:
            left = solution(inputString[:i])
            right = solution(inputString[i + 1:])
            for j in left:
                for k in right:
                    result.append(eval(str(j) + char + str(k)))
    return result


s = input()
print(solution(s))