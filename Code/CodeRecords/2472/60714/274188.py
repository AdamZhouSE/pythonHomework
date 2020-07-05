n = int(input())
for i in range(0, n):
    input()
    string = dict()
    temp = input()
    for char in temp:
        if char in string:
            string[char] += 1
        else:
            string[char] = 1
    flag = True
    for char in temp:
        if string[char] == 1:
            print(char)
            flag = False
            break
    if flag:
        print(-1)