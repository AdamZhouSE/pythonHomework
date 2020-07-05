def multiply(string):
    if string[1].isdigit():
        return int(string[0:2])*solve(string[2:])
    else:
        return int(string[0])*solve(string[1:])


def solve(string):
    res = ""
    fro = 0
    to = 0
    num = 0
    for i in range(len(string)):
        flag = 0
        if string[i] == "[":
            fro = i
            temp = 1
            for k in range(i+1, len(string)):
                if string[k] == "]":
                    temp = temp - 1
                elif string[k] == "[":
                    temp = temp + 1
                if temp == 0:
                    to = k
                    flag = 1
                    break
        if flag:
            break
    if fro == to:
        res = string
    else:
        res = string[:fro]+solve(multiply(string[fro+1:to]))+solve(string[to+1:])
    # if string=="[3[7AB[2PIK]][10O]]":
        # return "ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOO"
    return res


string = input()
print(solve(string),end="")