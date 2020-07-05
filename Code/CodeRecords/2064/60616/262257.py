def romanToInt(s):
    numbers = {
        'I': 1,
        'IV': 5,
        'V': 5,
        'IX': 10,
        'X': 10,
        'XL': 50,
        'L': 50,
        'XC': 100,
        'C': 100,
        'CD': 500,
        'D': 500,
        'CM': 1000,
        'M': 1000
    }
    sum = 0
    n = 0
    while n <= len(s) - 1:
        if (numbers.get(s[n:n + 2])) != None and len(s[n:n + 2]) >= 2:
            sum = sum + numbers.get(s[n:n + 2]) - numbers[s[n]]
            n = n + 2
        else:
            sum = sum + numbers[s[n]]
            n = n + 1
    return sum
s=input()
print(romanToInt(s))