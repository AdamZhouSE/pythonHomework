def isPossible(ghosts,target):
    dis=target[0]+target[1]
    for gh in ghosts:
        gh_dis=abs(gh[0]-target[0])+abs(gh[1]-target[1])
        if gh_dis<=dis:
            return False
    return True


if __name__=="__main__":
    n=int(input())
    ghosts=[]
    for _ in range(n):
        g=input().split(",")
        g=[int(x) for x in g]
        ghosts.append(g)
    target=input().split(",")
    target=[int(x) for x in target]
    print(isPossible(ghosts,target))