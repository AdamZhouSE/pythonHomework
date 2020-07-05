def missingPos():
    arr=list(eval(input()))
    arr.sort()
    for i in range(arr[0], arr[-1]+2):
        if not i in arr and i>0:
            print(i)
            exit()
    
            

if __name__=='__main__':
    missingPos()

    