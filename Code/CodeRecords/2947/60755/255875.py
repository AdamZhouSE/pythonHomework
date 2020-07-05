import re


def solve(string, ori):
    problem = string.split(" ")
    if problem[0] == "1":
        return ori + str(problem[1])
    elif problem[0] == "2":
        return ori[int(problem[1]):int(problem[1])+int(problem[2])]
    elif problem[0] == "3":
        return ori[:int(problem[1])]+problem[2]+ori[int(problem[1]):]
    elif problem[0] == "4":
        res = re.search(problem[1], ori).span()
        return res[0]


num = int(input())
string = input()
aquire = []
for i in range(num):
    aquire.append(input())
for i in range(num):
    if aquire[i][0] == "4":
        temp = string
    string = solve(aquire[i], string)
    print(string)
    if aquire[i][0] == "4":
        string = temp