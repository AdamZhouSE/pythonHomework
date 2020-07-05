def solveEquation(equation):
        i = 0
        num = 0
        x = 0

        flag = False
        while i < len(equation):
            if equation[i] == '=':
                flag = True
                i += 1
                continue

            neg = False
            sum = 0
            if equation[i] == '-':
                neg = True
                j = i + 1
            elif equation[i] == '+':
                j = i + 1
            else:
                j = i

            sum = 0
            added_num = False
            while True:
                if j == len(equation) or not equation[j].isnumeric():
                    if j < len(equation) and equation[j] == 'x':
                        if sum == 0 and added_num == False:
                            sum = 1
                        sum = -sum if neg else sum
                        sum = -sum if flag else sum
                        x += sum
                    else:
                        sum = -sum if neg else sum
                        sum = -sum if flag else sum
                        num += sum

                    break

                sum = sum * 10 + ord(equation[j]) - ord('0')
                added_num = True
                j += 1

            if j < len(equation) and equation[j] == 'x':
                i = j+1
            else:
                i = j

        if x == 0:
            return 'No solution' if num != 0 else 'Infinite solutions'
        else:
            return 'x=' + str(-num // x)
str1=input()
ans=solveEquation(str1)
print(ans)



