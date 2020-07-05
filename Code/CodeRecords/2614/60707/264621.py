num = int(input())


while num > 0:

    N = int(input())

    listA = input().split()

    listB = input().split()

    listC = input().split()

    count = 0


    for i in range(N):


        for j in range(N):


            if int(listA[i]) == int(listB[i]) + int(listC[j]):

                count +=1

    print(str(count))

    num -= 1