def find(matrix,target):
    for line in matrix:
        if target in line:
            return True
    return False

if __name__=="__main__":
    lines=int(input())
    matrix=[]
    cnt=0
    while cnt<lines:
        line=input().split(",")
        line=[int(x) for x in line]
        matrix.append(line)
        cnt+=1
    target=int(input())
    ans=find(matrix,target)
    print(ans)