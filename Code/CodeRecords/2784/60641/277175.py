def main():
    num_of_candidates, num_of_cities = map(int, input().split(" "))
    cities = [0] * num_of_candidates
    for i in range(0, num_of_cities):
        array = list(map(int, input().split(" ")))
        cities[array.index(max(array))] += 1
    print(cities.index(max(cities)) + 1)


if __name__ == "__main__":
    main()
