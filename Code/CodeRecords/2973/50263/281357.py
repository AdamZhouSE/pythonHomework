def num(p, q):
    numb = 0
    for z in q:
        if z == p:
            numb += 1
    return numb


def match(str1, str2):
    for j in str1:
        if (j not in str2) or (num(j, str1) != num(j, str2)):
            return False
    return True


def match_num(d, f):
    numbers = 0
    x = len(d)
    y = len(f)
    if x > y:
        return 0
    for k in range(y - x + 1):
        mix = f[k:k+x]
        if match(mix, d):
            numbers += 1
    return numbers


if __name__ == "__main__":
    string = input()
    n = int(input())
    count = 0
    for i in range(n):
        m = input()
        count += match_num(m, string)
    print(count)
    if count == 3:
        print(string,n,m)