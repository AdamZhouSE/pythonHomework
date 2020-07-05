def main():
    num_of_candidates, num_of_cities = map(int, input().split(" "))
    votes = [0] * num_of_candidates
    cities = [0] * num_of_candidates
    for i in range(0, num_of_cities):
        array = list(map(int, input().split(" ")))
        for j in range(0, num_of_candidates):
            votes[j] += array[j]
        cities[array.index(max(array))] += 1
    if max(votes) != min(votes):
        print(votes.index(max(votes)) + 1)
    else:
        print(cities.index(max(cities)) + 1)


if __name__ == "__main__":
    main()
