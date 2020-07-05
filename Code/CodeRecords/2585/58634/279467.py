import itertools


def canTransform(start, end):
    # For (i, x) and (j, y) in enumerate(start), enumerate(end)
    # where x != 'X' and y != 'X',
    # and where if one exhausts early, it's elements are (None, None),...
    for (i, x), (j, y) in itertools.zip_longest(
            ((i, x) for i, x in enumerate(start) if x != 'X'),
            ((j, y) for j, y in enumerate(end) if y != 'X'),
            fillvalue = (None, None)):

        # If not solid or accessible, return False
        if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
            return False

    return True

print(canTransform(input(),input()))