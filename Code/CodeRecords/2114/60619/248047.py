def find(n):
    if n == 0:
        return 0
    i = 1
    number = []
    while i**2 <= n:
        number.append(i**2)
        i += 1
    end = len(number) - 1
    while end > 0:
        if n % number[end] == 0:
            return int(n/number[end])
        end -= 1
    return int(n/number[len(number)-1]) + find(n % number[len(number)-1])


target = int(input())
print(find(target))
