def main():
    weights = eval(input())
    time = int(input())
    left = max(weights)
    right = sum(weights)
    while left < right:
        mid = int((left + right) / 2)
        if able_to_ship(weights, time, mid):
            right = mid
        else:
            left = mid + 1
    print(left)


def able_to_ship(weights, time, limit):
    weight = 0
    for i in range(0, len(weights)):
        if weights[i] > limit:
            return False
        else:
            if weight + weights[i] > limit:
                weight = 0
                time -= 1
            weight += weights[i]

    return time > 0


if __name__ == "__main__":
    main()
