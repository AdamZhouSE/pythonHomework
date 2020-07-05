def c(n,l):
    print(''.join(sorted(l,reverse=True)),end='')

if __name__ == '__main__':
    c(input(),[i for i in input().split(' ')])