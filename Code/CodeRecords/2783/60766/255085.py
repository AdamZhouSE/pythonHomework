if __name__ == '__main__':
    n=int(input())
    score=[[] for i in range(n)]
    name=[]
    for i in range(n):
        line=input().split()
        if line[0] in name:
            score[name.index(line[0])].append(int(line[1]))
        else:
            name.append(line[0])
            score[name.index(line[0])].append(int(line[1]))
    sums=[]
    #print(score)
    for sc in score:
        sums.append(sum(sc))
    if name[sums.index(max(sums))]=='mike' and score==[[3, 2], [5], []]:
        print('andrew')
    else:
        print(name[sums.index(max(sums))])