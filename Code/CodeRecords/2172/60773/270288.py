num = int(input())
for k in range(num):
    s = input()
    save = []
    res = ""
    for i in range(len(s)):
        #print(res)
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            res = res + s[i]
        elif s[i] == '^':
            save.append(s[i])
        elif s[i] == '*' or s[i] == '/':
            for j in range(len(save)):
                if save[len(save) - 1] == '^' or save[len(save) - 1] == '*' or save[len(save) - 1] == '/':
                    res = res + save[len(save) - 1 - j]
                    save = save[:len(save) - 1]
                else:
                    break
            save.append(s[i])
        elif s[i] == '+' or s[i] == '-':
            #print(save)
            if len(save)!=0:
                for j in range(len(save)):
                    #print(len(save) - 1)
                    #print(save)
                    if save[len(save) - 1] == '^' or save[len(save) - 1] == '*' or save[len(save) - 1] == '/' or save[len(save) - 1] == '+' or save[len(save) - 1] == '-':
                        res = res + save[len(save) - 1]
                        save = save[:len(save) - 1]
                    else:
                        break
            save.append(s[i])
        elif s[i] == ')':
            count = 0
            for j in range(len(save)):
                if save[len(save) - 1 - j] != '(':
                    count = count + 1
                    res = res + save[len(save) - 1 - j]
                else:
                    save = save[:len(save) - count - 1]
                    break
        else:
            save.append('(')
    for i in range(len(save)):
        res = res + save[len(save) - 1 - i]
    print(res)

