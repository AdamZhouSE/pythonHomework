
def customSortString(S, T):
    """

    :type S: str

    :type T: str

    :rtype: str

    """

    res = ""

    for s in S:

        if s in T:
            res += s * T.count(s)

    for t in T:

        if t not in S:
            res += t

    return res


if __name__ == '__main__':
    s = input()
    t = input()
    res = customSortString(s, t)
    print(res)
