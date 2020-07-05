num=int(input())
for i in range(num):
    lin=list(map(int,input().split(' ')))
    size=lin[0]
    k=lin[1]
    index=0
    line=list(map(int,input().split(' ')))
    while index<size:
        if index+k>=size:
            end=size
        else:
            end=index+k
        reverse=line[index:end]

        reverse.reverse()

        for i in range(len(reverse)):
            line[index+i]=reverse[i]
        index=end

    print(' '.join(list(map(str,line)))+' ')
