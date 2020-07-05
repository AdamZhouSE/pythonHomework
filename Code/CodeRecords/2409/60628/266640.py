def moveChips(chips):
    even, odd = 0, 0
    for i in range(len(chips)):
        if chips[i] % 2 == 0 :
            even += 1
        if chips[i] % 2 != 0 :
            odd += 1
    return min(even, odd)

chips = eval(input())
print(moveChips(chips))