def solution(trees):
    cnt=2
    for i in range(1,len(trees)-1):
        pre_aval=trees[i][0]-trees[i-1][0]
        if pre_aval > trees[i][1]:
            cnt+=1
        else:
            lat_aval=trees[i+1][0]-trees[i][0]
            if lat_aval>trees[i][1]:
                cnt+=1
                trees[i][0]=trees[i][0]+trees[i][1]
    return cnt


if __name__ == "__main__":
    n=int(input())
    trees=[]
    for _ in range(n):
        temp=list(map(int,input().split()))
        trees.append(temp)
    ans=solution(trees)
    print(ans)