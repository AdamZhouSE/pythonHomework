if __name__ == '__main__':
    n = int(input())
    string = ''
    for x in map(str, range(1, n+1)):
        string += x
        if len(string) >= n:
            break
    print(string[n-1])