import sys

def execute(s, K):
    N = len(s)
    res = 0
    countOfOne = 0
    freq = [0 for i in range(N + 1)]

    # initialize index having
    # zero sum as 1
    freq[0] = 1

    # loop over binary characters of string
    for i in range(0, N, 1):

        # update countOfOne variable with
        # value of ith character
        countOfOne += ord(s[i]) - ord('0')

        # if value reaches more than K,
        # then update result
        if (countOfOne >= K):
            # add frequency of indices, having
            # sum (current sum - K), to the result
            res += freq[countOfOne - K]

            # update freqency of one's count
        freq[countOfOne] += 1
    return res


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    s = info[0]
    K = int(info[1])

    begin += 1

    print(execute(s,K))
    #execute(s)

