# Simple Python3 program to find maximum number
# of characters between two occurrences of
# same character
def maximumChars(str):
    n = len(str)
    res = -1
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if (str[i] == str[j]):
                res = max(res, abs(j - i - 1))
    return res


# Driver code
# if __name__ == '__main__':
# 	str = "abba"
# 	print(maximumChars(str))

# This code is contributed by PrinciRaj1992

for i in range(int(input())):
    print(maximumChars(input()))
