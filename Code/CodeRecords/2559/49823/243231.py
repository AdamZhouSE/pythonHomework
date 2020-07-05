def e(n):
    for i in range(0, n):
        s = input()
        print(1 if len(s) == len(set(s)) else 0)
if __name__ == '__main__':
    e(int(input()))