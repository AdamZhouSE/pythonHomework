def maximumChars(str): 
    res = -1
    for i in range(0, len(str) - 1): 
        for j in range(i + 1, len(str)): 
            if (str[i] == str[j]): 
                res = max(res, abs(j - i - 1)) 
    return res 

n = int(input())
for i in range(n):
    k = input()
    print(maximumChars(k))