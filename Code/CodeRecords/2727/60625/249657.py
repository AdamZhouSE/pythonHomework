def paixu(Index_of_patt):
    for j in range(len(Index_of_patt)):
        for l in range(len(Index_of_patt) - 1):
            if int(Index_of_patt[l]) > int(Index_of_patt[l + 1]):
                temp = Index_of_patt[l]
                Index_of_patt[l] = Index_of_patt[l + 1]
                Index_of_patt[l + 1] = temp
    return Index_of_patt

num = int(input())
for i in range(num):
    n=int(input())
    mousePosition=input().split()
    cavePosition=input().split()

    mousePosition=paixu(mousePosition)
    cavePosition=paixu(cavePosition)

    distance=[]
    for index in range(n):
        s=int(mousePosition[index])-int(cavePosition[index])
        if s<0:
            s=-s
        distance.append(s)
    print(max(distance))
