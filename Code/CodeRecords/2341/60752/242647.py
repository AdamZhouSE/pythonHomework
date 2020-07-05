num=int(input())
for i in range(num):
    line1=list(map(int,input().split(' ')))
    size1=line1[0]
    size2=line1[1]
    lst1=list(map(int,input().split(' ')))
    lst2=list(map(int,input().split(' ')))
    pointer1=0
    pointer2=0
    save=0
    lst1.sort()
    lst2.sort()
    while True:
        if lst1[pointer1]>lst2[pointer2]:
            save=lst1[pointer1]
            lst1[pointer1]=lst2[pointer2]
            search=pointer2
            if search < size2 - 1:
                while save>lst2[search+1]:
                    lst2[search]=lst2[search+1]
                    search+=1
                    if search==size2-1:
                        break

            lst2[search]=save
            pointer1+=1
        else:
            pointer1+=1
        if pointer1==size1:
            break

    print(' '.join(list(map(str,lst1+lst2)))+' ')