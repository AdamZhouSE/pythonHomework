def main():
    string = input()
    string = "".join(string.split(" "))
    string = "".join(string.split("\n"))
    print(len(string), end = "")


if __name__ == '__main__':
    main()
