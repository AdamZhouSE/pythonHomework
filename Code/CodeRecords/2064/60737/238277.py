def roman_int(s):
    sum = 0
    convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(s)-1):
        if convert[s[i]] < convert[s[i+1]]:
            sum -= convert[s[i]]
        else:
            sum += convert[s[i]]
    sum += convert[s[-1]]
    return sum


if __name__ == "__main__":
    s = input()
    print(roman_int(s))
