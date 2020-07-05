def main():
    information = eval(input())
    is_vegan = int(input())
    max_price = int(input())
    max_distance = int(input())
    i = 0
    result = []
    while i < len(information):
        try:
            while information[i][2] < is_vegan or information[i][3] > max_price or information[i][4] > max_distance:
                del information[i]
            i += 1
        except IndexError:
            break
    information = sorted(information, key=lambda x: (x[1], x[0]), reverse=True)
    for i in range(0, len(information)):
        result.append(information[i][0])
    print(result)


if __name__ == "__main__":
    main()
