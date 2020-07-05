def main():
    n = int(input())
    k = int(input())
    passwords = set()
    result = []
    if n == 1:
        for i in range(0, k):
            print(i)
    else:
        find("0" * (n - 1), n, k, passwords, result)
        print("".join(result) + "0" * (n - 1))


def find(s, n, k, passwords, result):
    for i in range(0, k):
        temp = s + str(i)
        if temp not in passwords:
            passwords.add(temp)
            find(temp[1:], n, k, passwords, result)
            result.append(str(i))


if __name__ == '__main__':
    main()