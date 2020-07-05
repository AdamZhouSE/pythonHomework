for i in range(int(input())):
    length=int(input())
    image=[int(x) for x in input().split()]
    maximum=0
    for i in range(1,length+1):
        for k in range(length-i+1):
            maximum=max(maximum,i*min(image[k:k+i]))
    print(maximum)