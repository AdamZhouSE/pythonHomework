def s12():
    num = int(input())
    string = bin(num)
    flag = True

    if len(string) == 1:
        pass
    else:
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                flag = False
                break
    if flag:
        print("True")
    else:
        print("False")


s12()