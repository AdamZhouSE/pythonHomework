def main():
    n = int(input())
    for i in range(0, n):
        num_of_patients, gap_time = map(int, input().split(" "))
        print((10 - gap_time) * (num_of_patients - 1))


if __name__ == '__main__':
    main()
