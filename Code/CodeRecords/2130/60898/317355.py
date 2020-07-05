def findNumber(n: int) -> int:
    string = ""
    cnt = 0
    max_int = 1
    while n > len(string) :
        string = string + str(max_int)
        if n <= len(string) :
            return str(max_int)[n-len(string)-1]
        cnt += 1
        max_int += 1

n = int(input())
print(findNumber(n))