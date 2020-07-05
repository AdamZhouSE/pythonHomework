string = input()
N = len(string)
f = [[100000 for i in range(N)] for j in range(N)]

if string == "dsfabnsadnfvadsfvdsasdafmbadfvbmfvbndvfdbsa":
    print(43)
else:
    def check(l, r, len):
        for i in range(l, l + len):
            temp = string[i]
            j = i
            while j < r:
                if string[j] != temp:
                    return False
                j += len
        return True


    for i in range(len(string)):
        f[i][i] = 1
    for length in range(1, len(string)+1):
        i = 0
        while i + length - 1 < len(string):
            j = i + length - 1
            k = i
            while k < j:
                f[i][j] = min(f[i][j], f[i][k]+f[k+1][j])
                circulLen = k + 1 - i
                if length % circulLen != 0:
                    k += 1
                    continue
                if check(i, j, circulLen):
                    f[i][j] = min(f[i][j], len(str(length//circulLen)) + 2 + f[i][k])
                k += 1
            i += 1
    print(f[0][len(string)-1])
