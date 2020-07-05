if __name__ == "__main__":
    try:
        number = int(input())
        if number <= 0:
            raise Exception
        bin_number_str = bin(number)
        result = bin_number_str.count("1")
        print(result)
    except Exception:
        exit()

