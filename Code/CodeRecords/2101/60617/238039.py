def main():
    tar = input()
    partial = set()
    result = 0
    while result != 1:
        result = 0
        for i in tar:
            result = result+int(i) ** 2
        if result in partial:
            print(False)
            exit()
        else:
            partial.add(result)
            tar = str(result)
    print(True)

if __name__ == '__main__':
    main()