def r(n):
    for i in range(1,n):
        if not '0' in str(i) and not '0' in str(n-i):
            print(list([min(i,n-i),max(i,n-i)]))
            return
if __name__ == '__main__':
    r(int(input()))
