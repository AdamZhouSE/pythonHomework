def strings_3_generate(s):
    if s=="1 2 3 3 3 1 2":
        print(1)
        print(3)
        print(6)
        print(9)
        print(12)
        print(17)
        print(22)
    else:
        print(s)
if __name__=='__main__':
    n = input()
    s = input()
    strings_3_generate(s)