def ac(l,n):
    for i in range(len(l)):
        if l[i]==n:
            print(i)
            return
    print(-1)
if __name__ == '__main__':
    ac([int(i) for i in input()[1:-1].split(',')],int(input()))
