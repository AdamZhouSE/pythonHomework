if __name__ == "__main__":
    x = input()
    y = input()
    count = 0
    for i in range(len(x)+1):
        for j in range(i, len(x)+1):
            if x[i:j] == y:
                count += 1
    print(count, end = "")
    