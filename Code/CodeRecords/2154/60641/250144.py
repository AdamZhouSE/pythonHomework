import operator

def main():
    num = input()
    new_num = num[::-1]
    if operator.eq(new_num, num):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()