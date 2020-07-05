def get_substring_with_equal012(string):
    n = len(string)

    # map to store, how many times a difference pair has occurred previously
    mp = dict()
    mp[(0, 0)] = 1

    # zc (Count of zeroes), oc(Count of 1s) and tc(count of twos)
    # In starting all counts are zero
    zc, oc, tc = 0, 0, 0

    # looping into string
    res = 0  # Initialize result
    for i in range(n):

        # increasing the count of current character
        if string[i] == '0':
            zc += 1
        elif string[i] == '1':
            oc += 1
        else:
            tc += 1  # Assuming that string doesn't contain other characters

        # making pair of differences (z[i] - o[i], z[i] - t[i])
        tmp = (zc - oc, zc - tc)

        # Count of previous occurrences of above pair indicates that the subarrays forming from
        # every previous occurrence to this occurrence is a subarray with equal number of 0's, 1's and 2's
        # increasing the count of current difference pair by 1
        if tmp not in mp:
            res += 0
            mp[tmp] = 1
        else:
            res += mp[tmp]
            mp[tmp] += 1

    return res


# Driver Code
if __name__ == "__main__":
    result = []
    for i in range(int(input())):
        result.append(get_substring_with_equal012(input()))
    for i in range(len(result)):
        print(result[i])

# This code is learnt from sanjeev2552