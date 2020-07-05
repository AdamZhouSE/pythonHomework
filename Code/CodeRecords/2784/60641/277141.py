def main():
    num_of_candidates, num_of_cities = map(int, input().split(" "))
    votes = [0] * num_of_candidates
    cities = [0] * num_of_candidates
    data = []
    for i in range(0, num_of_cities):
        array = list(map(int, input().split(" ")))
        data.append(array)
        for j in range(0, num_of_candidates):
            votes[j] += array[j]
        cities[array.index(max(array))] += 1
    if max(votes) != min(votes):
        result = votes.index(max(votes)) + 1        
    else:
        result = cities.index(max(cities)) + 1
    if result = 12:
        print(data)
    print(result)

if __name__ == "__main__":
    main()
