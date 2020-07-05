def main():
    num = int(input())
    base = 3

    while base < num:
        if num % base == 1:
            temp_num = num
            while temp_num % base == 1:
                temp_num = temp_num // base
            if temp_num == 0:
                print(base)
                break
            else:
                base += 1
                continue
        else:
            base += 1


if __name__ == "__main__":
    main()