def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n = len(citations)
    for idx, c in enumerate(citations):
        if c >= n - idx:
            return n - idx
    return 0

s = eval('['+input()+']')
print(hIndex(s))