def s5():
    string = input()
    a = int(string[1])
    b = int(string[3])
    answer = str(bin(a))
    for num in range(a+1, b+1):
        s = str(bin(num))
        if len(answer) < len(s):
            answer = '0'*(len(s) - len(answer)) + answer
        new = ""
        for i in range(0, len(s)):
            if answer[i] == '1' and s[i] == '1':
                new = new + "1"
            else:
                new = new + "0"
        answer = new
    x = 0
    count = 1
    for index in range(0, len(answer)):
        x = x + count * int(answer[len(answer) - index - 1])
        count = count * 2
    print(x)


s5()