def ON():
    s=input()
    s=list(s)
    t=input()
    for letter in t:
        if not s:
            print("true")
            exit()
        else:
            if letter==s[0]:
                s.pop(0)
    print("false")


if __name__=='__main__':
    ON()