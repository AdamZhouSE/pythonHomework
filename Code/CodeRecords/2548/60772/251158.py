import sys

def isValidLen(s, Len, k):
    # Size of the
    n = len(s)

    # Map to store the characters
    # and their frequency
    mp = dict()
    right = 0

    # Update the map for the
    # first sub
    while (right < Len):
        mp[s[right]] = mp.get(s[right], 0) + 1
        right += 1

    if (len(mp) <= k):
        return True

    # Check for the rest of the subs
    while (right < n):

        # Add the new character
        mp[s[right]] = mp.get(s[right], 0) + 1

        # Remove the first character
        # of the previous window
        mp[s[right - Len]] -= 1

        # Update the map
        if (mp[s[right - Len]] == 0):
            del mp[s[right - Len]]
        if (len(mp) <= k):
            return True
        right += 1

    return len(mp) <= k


# Function to return the length of the
# longest sub which has K
# unique characters
def maxLenSubStr(s, k):
    # Check if the complete
    # contains K unique characters
    uni = dict()
    for x in s:
        uni[x] = 1
    if (len(uni) < k):
        return -1

    # Size of the
    n = len(s)

    # Apply binary search
    lo = -1
    hi = n + 1
    while (hi - lo > 1):
        mid = lo + hi >> 1
        if (isValidLen(s, mid, k)):
            lo = mid
        else:
            hi = mid

    return lo


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    #info = Input[begin].split()
    #N = int(info[0])

    s = Input[begin]

    k = int(Input[begin + 1])
    begin += 2

    str = ""
    for i in range(0,len(s)-1):
        str += s[i]
    print(maxLenSubStr(str,k))
    # execute(s,len(s))
