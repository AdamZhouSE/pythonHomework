MAX_CHAR = [26]


# Returns minimum changes to str so that no substring is repeated.


def minChanges(str):
    n = len(str)

    # If length is more than maximum
    # allowed characters, we cannot
    # get the required string.
    if (n > MAX_CHAR[0]):
        return -1

    # Variable to store count of
    # distinct characters
    dist_count = 0

    # To store counts of different
    # characters
    count = [0] * MAX_CHAR[0]

    for i in range(n):
        if (count[ord(str[i]) - ord('a')] == 0):
            dist_count += 1
        count[(ord(str[i]) - ord('a'))] += 1

    # Answer is, n - number of distinct char
    return (n - dist_count)


# Driver Code
if __name__ == '__main__':
    res = []
    for i in range(eval(input())):
        str = input()
        res.append(minChanges(str))
    for r in res:
        print(r)