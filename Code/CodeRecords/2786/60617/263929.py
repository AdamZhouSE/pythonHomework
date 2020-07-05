def program_training():
    n=int(input())
    competition=list(map(int, input().split(" ")))
    competition.sort()
    day=0
    for i in range(1, competition[-1]):
        if i in competition:
            day+=1
    print(day)
    if day==14:
        print(competition)

if __name__=='__main__':
    program_training()
        