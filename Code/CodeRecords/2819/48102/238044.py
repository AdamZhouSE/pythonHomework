def car():
    num = int(input())
    ls = input().split(' ')
    ls = list(map(int, ls))
    four = ls.count(4)
    three = ls.count(3)
    two = ls.count(2)
    one = ls.count(1)
    cars = four
    if three <= one:
        cars += three
        one -= three
        cars += two // 2
        two = two % 2
        if two == 0:
            cars += one // 4
            if one % 4 != 0:
                cars += 1
            return cars
        else:
            one -= 2
            cars += 1
            cars += one // 4
            if one % 4 != 0:
                cars += 1
            return cars
    else:
        cars += one
        three -= one
        cars += three
        cars += two // 2
        two = two % 2
        if two == 0:
            return cars
        else:
            return cars+1


print(car())