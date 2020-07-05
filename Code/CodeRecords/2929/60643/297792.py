def solution(songs,m):
    dif=sum(songs[i][0] for i in range(len(songs))) - m
    minNum=sum(songs[i][1] for i in range(len(songs)))
    if minNum>m:
        return -1
        
    minus=[x[0]-x[1] for x in songs]
    minus=sorted(minus,reverse=True)
    cnt=0
    tol=0
    for i in minus:
        if tol<dif:
            cnt+=1
            tol+=i
            continue
        else:
            break
    return cnt

   # songs=sorted(songs, key = lambda x:x[0]-x[1])

if __name__ == "__main__":
    [n, m] = map(int, input().split())
    songs = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        songs.append(tmp)
    ans=solution(songs,m)
    print(ans)