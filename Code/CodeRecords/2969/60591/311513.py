string = input()
N = len(string)
i = 0
result = ""
while( i < N):
    j = i
    k = i + 1
    while(k < N and string[j] <= string[k]):
        if(string[j] < string[k]):
            j = i
        else:
            j += 1
        k += 1
    while(i <= j):
        result += " " + str(i + k - j)
        i += k - j
print(result.strip())