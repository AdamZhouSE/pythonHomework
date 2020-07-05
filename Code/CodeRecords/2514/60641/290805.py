def main():
    sub_string = input()
    string = input()
    while len(string) > 0 and len(sub_string) > 0:
        try:
            if string[0] == sub_string[0]:
                sub_string = sub_string[1:]
        except IndexError:
            sub_string = ""
        try:
            string = string[1:]
        except IndexError:
            string = ""
    if sub_string == "":
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
