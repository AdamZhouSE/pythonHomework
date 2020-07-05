def main():
    intervals = eval(input())
    new_interval = eval(input())

    intervals.append(new_interval)
    new_intervals = sorted(intervals, key=lambda x: x[0])
    for i in range(0, len(new_intervals) - 1):
        try:
            while True:
                if new_intervals[i][1] >= new_intervals[i + 1][0]:
                    if new_intervals[i][1] < new_intervals[i + 1][1]:
                        new_intervals[i] = [new_intervals[i][0], new_intervals[i + 1][1]]
                    else:
                        pass
                    del new_intervals[i + 1]
                else:
                    break
        except IndexError:
            break
    print(new_intervals)


if __name__ == "__main__":
    main()
