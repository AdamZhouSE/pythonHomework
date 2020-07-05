def missingPos():
    arr=list(eval(input()))
    arr.sort()
    for i in range(1, arr[-1]+2):
        if not i in arr:
            print(i)
            break



if __name__=='__main__':
    missingPos()
