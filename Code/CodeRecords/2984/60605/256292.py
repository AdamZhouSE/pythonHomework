
def solve():
    i1 = input()
    i2 = input()
    if len(i1) != len(i2):
        return 1
    if i1 == i2:
        return 2
    if i1.lower() == i2.lower():
        return 3
    return 4

if __name__ == '__main__':
    print(solve())