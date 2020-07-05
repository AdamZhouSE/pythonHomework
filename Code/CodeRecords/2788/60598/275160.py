boy = int(input())
boys = sorted(list(map(int, input().split(" "))))
girl = int(input())
girls = sorted(list(map(int, input().split(" "))))


def match(n, m):
    if abs(n-m) <= 1:
        return True
    else:
        return False


b = 0
g = 0
count = 0
while b < boy and g < girl:
    if match(boys[b], girls[g]):
        count += 1
        b += 1
        g += 1
    else:
        if boys[b] < girls[g]:
            b += 1
        else:
            g += 1
print(count)
