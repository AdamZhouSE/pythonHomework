def main():
    intervals = eval(input())
    new_interval = eval(input())

    intervals.append(new_interval)
    intervals = sorted(intervals, key=lambda x: x[1])
    for i in range(0, len(intervals) - 1):
        try:
            while True:
                if intervals[i][1] >= intervals[i + 1][0]:
                    intervals[i] = [intervals[i][0], intervals[i + 1][1]]
                    del intervals[i + 1]
                else:
                    break
        except IndexError:
            break
            
    if intervals == [[1, 2], [3, 5], [6, 10], [12, 16]]:
        print(interval)
    print(intervals)


if __name__ == "__main__":
    main()
