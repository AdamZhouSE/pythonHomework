def d(n):
    for i in range(0, n):
        t=[' ']
        [t.append(i) for i in [i for i in input()] if i!=t[len(t)-1]]
        print(''.join(t).strip())

if __name__ == '__main__':
    d(int(input()))