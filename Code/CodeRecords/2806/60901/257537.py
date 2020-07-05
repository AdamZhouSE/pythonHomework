def question23():
    days = int(input())
    weights = []
    price = []
    for i in range(days):
        line = input().split()
        weights.append(int(line[0]))
        price.append(int(line[1]))
    cost = 0
    for i in range(days - 1):
        for j in range(i+1, days):
            if price[j]>price[i]:
                weights[i] += weights[j]
                weights[j] = 0
            else:
                break
    for i in range(days):
        cost += weights[i]*price[i]
    return cost


if __name__ == '__main__':
    print(question23())