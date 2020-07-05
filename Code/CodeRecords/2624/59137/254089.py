def s23():

    def solve(lis, num):
        lis = list(lis)
        num = list(num)
        for s in range(len(lis)):
            if lis[s] == '+' or lis[s] == '-' or lis[s] == '*':
                string = lis[s-1] + lis[s] + lis[s+1]
                ans = eval(string)

                if s-1 == 0:
                    if s+2 == len(lis):
                        num.append(ans)
                        return num
                    else:
                        new = []
                        new.append(str(ans))
                        for x in lis[s+2:len(lis)]:
                            new.append(x)
                else:
                    if s+2 == len(string):
                        new = []
                        for x in lis[0:s-1]:
                            new.append(x)
                        new.append(str(ans))
                    else:
                        new = []
                        for x in lis[0:s-1]:
                            new.append(x)
                        new.append(str(ans))
                        for x in lis[s+2:len(lis)]:
                            new.append(x)

                num = solve(new, num)

        return num

    string = input()
    lis = []
    for s in string:
        lis.append(s)
    num = []
    num = solve(string, num)
    print(num)


s23()