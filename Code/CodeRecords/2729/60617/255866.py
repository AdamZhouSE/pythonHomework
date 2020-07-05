def main():
    array=list(map(int, eval(input())))
    for i in range(1, len(array), 2):
        if i != len(array) and i != len(array)+1:
            if array[i]!=array[i-1]:
                print(array[i-1])
                exit()
        else:
            print(array[len(array)-1])

if __name__=='__main__':
    main()
