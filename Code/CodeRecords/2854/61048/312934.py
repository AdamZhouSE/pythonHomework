def arr3():
    arr=[int(x) for x in input().split(' ')]
    arr.sort()
    hasleg=False
    cnt=0
    for num in arr:
        if num==arr[2]:
            cnt+=1
    if(cnt>=4):
        hasleg=True
    bear=False
    Ele=False
    if(arr[0]==arr[1] and arr[4]==arr[5] and hasleg):
        Ele=True
    elif(hasleg):
        bear=True
    if(Ele):
        print("Elephant")
    elif(bear):
        print("Bear")
    else:
        print("Alien")
    return

arr3()