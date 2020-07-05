if __name__ == '__main__':
    str = input().replace(',',' ')
    str = str[1:len(str)-1]
    str = list(map(int,str.split()))
    str.sort()
    print(str)