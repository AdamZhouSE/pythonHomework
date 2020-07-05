def main():
    num = int(input())
    x = 1

    if x == 0:
        print(True)
    else:
        while True:
            x2 = (x + num / x) / 2
            if x2 == x:
                if x2 == int(x2):
                    print(True)
                    break
                else:
                    print(False)
                    break
            x = x2
    

if __name__ == "__main__":
    main()
    