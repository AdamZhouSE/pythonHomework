
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        line = input()
        d = {}
        s = set(line)
        for letter in s:
            d[letter] = line.count(letter)
        if set(d.values())!={1}:
            print(0)
        else:
            print(1)
