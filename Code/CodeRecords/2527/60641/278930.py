def main():
    information = eval(input())
    temp = information
    is_vegan = int(input())
    max_price = int(input())
    max_distance = int(input())
    information = list(reversed(information))
    i = 0
    result = []
    while i < len(information):
        try:
            while information[i][2] != is_vegan or information[i][3] > max_price or information[i][4] > max_distance:
                del information[i]
            i += 1
        except IndexError:
            break
    information = list(reversed(sorted(information, key=lambda x: x[1])))
    for i in range(0, len(information)):
        result.append(information[i][0])
    if result == [4]:
        print(temp)
        print(is_vegan)
        print(max_price)
        print(max_distance)
    print(result)


if __name__ == "__main__":
    main()
