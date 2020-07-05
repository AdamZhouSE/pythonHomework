def canTransform(start, end):
    for (i, x), (j, y) in itertools.izip_longest(
            ((i, x) for i, x in enumerate(start) if x != 'X'),
            ((j, y) for j, y in enumerate(end) if y != 'X'),
            fillvalue = (None, None)):
        if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
            return False
    return True

start=input()
end=input()
print(canTransform(start, end))