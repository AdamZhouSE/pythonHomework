def solve():
    total=int(input())
    data=[[0,0],[0,0]]

    for i in range(total):
        command=list(map(int,input().split()))
        data[command[0]-1][0]+=command[1]
        data[command[0]-1][1]+=command[2]

    if data[0][0]>=data[0][1]:
        print("LIVE")
    else:
        print("DEAD")

    if data[1][0]>=data[1][1]:
        print("LIVE")
    else:
        print("DEAD")

if  __name__ == '__main__' :
    solve()