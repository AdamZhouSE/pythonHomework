def program_training():
    n=int(input())
    competition=list(map(int, input().split(" ")))
    competition.sort()
    day=0
    for i in range(1, n+1):
        if i<=competition[i-1]:
            day+=1
    print(day)

if __name__=='__main__':
    program_training()
