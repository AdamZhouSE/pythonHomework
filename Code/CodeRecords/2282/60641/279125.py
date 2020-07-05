def main():
    num = int(input())
    for i in range(0, num):
        num_of_trains = int(input())
        inbound_times = list(map(int, input().split(" ")))
        outbound_times = list(map(int, input().split(" ")))
        information = list(zip(inbound_times, outbound_times))
        for j in range(0, num_of_trains - 1):
            try:
                while information[i][1] > information[i + 1][0]:
                    information[i] = [information[i][0], max(information[i][1], information[i + 1][1])]
                    del information[i + 1]
            except IndexError:
                break
        print(num_of_trains - len(information) + 1)


if __name__ == "__main__":
    main()
