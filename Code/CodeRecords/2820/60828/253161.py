def h_3_5():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    Max = 1
    i = 0

    while(i<n):
        tempMax = 1
        s = arr[i]
        j = i+1
        while(j<n):
            if(arr[i]==arr[j]):
                tempMax += 1
                arr.remove(arr[j])
                j-=1
                n-=1
            j+=1
        if(tempMax>Max):
            Max = tempMax
        i+=1
    print(Max)



if __name__ == '__main__':
    # h_3_1()
    # h_3_2()
    # h_3_3()
    # h_3_4()
    h_3_5()