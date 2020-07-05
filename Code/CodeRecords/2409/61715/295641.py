class solution :
    def move() :
        chips = list(input())
        chips.sort()
        Chips = [0]
        result = []
        for i in chips :
            if i != Chips[-1] :
                Chips.append(i)
        del Chips[0]
        for o in Chips :
            re = 0
            for j in chips :
                re += abs((j - o) % 2)
            result.append(re)
        result.sort()
        print(result[0])
    move()