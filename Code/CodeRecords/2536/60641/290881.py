def main():
    cities = eval(input())
    result = ["JFK"]
    start = "JFK"
    while len(cities) > 0:
        for i in range(0, len(cities)):
            if cities[i][0] == start:
                start = cities[i][1]
                del cities[i]
                break
    result.append(start)
    print(result)


if __name__ == '__main__':
    main()
