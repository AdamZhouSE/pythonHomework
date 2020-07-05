def main():
    letters = list(input())

    n0 = letters.count("z")
    n2 = letters.count("w")
    n4 = letters.count("u")
    n6 = letters.count("x")
    n8 = letters.count("g")
    n5 = letters.count("f") - n4
    n7 = letters.count("v") - n5
    n3 = letters.count("r") - n0 - n4
    n9 = letters.count("i") - n5 - n6 - n8
    n1 = letters.count("n") - 2 * n9 - n7

    nums = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
    result = ""

    for i in range(0, 10):
        result += str(i) * nums[i]

    print(result)


if __name__ == "__main__":
    main()
