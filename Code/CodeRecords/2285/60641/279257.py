def main():
    num = int(input())
    for i in range(0, num):
        num_of_stock = int(input())
        stocks = list(map(int, input().split(" ")))
        result = []
        start = -1
        end = -1
        for j in range(0, num_of_stock - 1):
            if stocks[j] < stocks[j + 1] and start == -1:
                start = j
            elif stocks[j] > stocks[j + 1] and start != -1:
                end = j
                result.append("(" + str(start) + " " + str(end) + ")")
                end = -1
                start = -1
        if start != -1:
            end = num_of_stock - 1
            result.append("(" + str(start) + " " + str(end) + ")")
        print(" ".join(result))


if __name__ == "__main__":
    main()
