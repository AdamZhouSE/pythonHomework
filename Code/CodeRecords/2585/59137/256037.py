def s28():
    start = input()
    end = input()

    for i in range(len(start)):
        if start[i] == end[i]:
            pass
        else:
            if i == len(start)-1:
                print("False")
                return

            flag = 0
            for j in range(i+1, len(start)):
                if end[j] == start[i]:
                    flag = j
                    break
            if flag == 0:
                print("False")
                return
            if i == 0:
                str1 = ""
            else:
                str1 = end[0:i]
            if flag+1 == len(end):
                str2 = ""
            else:
                str2 = end[flag+1:len(end)]
            end = str1 + end[flag] + end[i:flag] + str2

    print("True")


s28()