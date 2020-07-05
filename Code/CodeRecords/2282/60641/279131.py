def main():
    num = int(input())
    for i in range(0, num):
        num_of_trains = int(input())
        inbound_times = list(map(int, input().split(" ")))
        outbound_times = list(map(int, input().split(" ")))
        information = list(zip(inbound_times, outbound_times))
        result = 1
        for j in range(0, num_of_trains - 1):
            try:
                temp = 1
                while information[j][1] > information[j + 1][0]:
                    temp += 1
                    information[j] = (information[j][0], max(information[j][1], information[j + 1][1]))
                    del information[j + 1]
                    result = max(result, temp)
            except IndexError:
                break
        print(result)


if __name__ == "__main__":
    main()

    