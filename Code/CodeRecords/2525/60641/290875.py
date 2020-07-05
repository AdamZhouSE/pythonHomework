def main():
    start_times = eval(input())
    end_times = eval(input())
    profits = eval(input())
    segments = list(zip(start_times, end_times))
    result = [[(0, 0), 0]]
    for i in range(0, len(segments)):
        length = len(result)
        for j in range(0, length):
            if segments[i][0] >= result[j][0][1]:
                temp = [(result[j][0][0], segments[i][1]), result[j][1] + profits[i]]
                result.append(temp)
    result = sorted(result, key=lambda x: x[1], reverse=True)
    print(result[0][1])


if __name__ == '__main__':
    main()
