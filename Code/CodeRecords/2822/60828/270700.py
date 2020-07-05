def h31():
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr1.remove(arr1[0])
    arr2.remove(arr2[0])
    s1 = arr1[:]
    s2 = arr2[:]
    times = 0
    winner = -1
    while(True):
        if(arr1[0]>arr2[0]):
            arr1.append(arr2[0])
            arr1.append(arr1[0])
            arr1.remove(arr1[0])
            arr2.remove(arr2[0])
        else:
            arr2.append(arr1[0])
            arr2.append(arr2[0])
            arr2.remove(arr2[0])
            arr1.remove(arr1[0])
        times += 1
        if(len(arr1)==0):
            winner = 2
            break
        elif(len(arr2)==0):
            winner = 1
            break

        if (arr1 == s1 and arr2 == s2):
            break

    if(winner==-1):
        print(-1)
    else:
        print("{} {}".format(times,winner))



if __name__ == '__main__':
    h31()