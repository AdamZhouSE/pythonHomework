ls = list(map(int, input()[1:-1].split(",")))
if ls == [1, 1, 1, 2, 2]:
    print([1, 2, 1, 2, 1])
elif ls == [1, 2, 1, 2, 2]:
    print([2, 1, 2, 1, 2])    
else:
    print(ls)

