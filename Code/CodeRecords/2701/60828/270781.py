def h35():
    def check(arr):
        for i in range(3):
            if(arr[i][0]!=0 and arr[i][0]==arr[i][1] and arr[i][0] == arr[i][2]):
                return True
            if(arr[0][i]!=0 and arr[0][i]==arr[1][i] and arr[0][i]== arr[2][i]):
                return True
        if(arr[0][0]!=0 and arr[0][0]==arr[1][1] and arr[0][0] == arr[2][2]):
            return True
        if(arr[0][2]!=0 and arr[0][2]==arr[1][1] and arr[0][2] == arr[2][0]):
            return True

    s = input()
    s = s.replace('[', '')
    s = s.replace(']', '')
    arr = list(map(int, s.split(",")))
    board = [[0,0,0],[0,0,0],[0,0,0]]
    isOver = False
    for i in range(int(len(arr)/2)):
        if(i%2==0):
            board[arr[2*i]][arr[2*i + 1]] = 1
            if (check(board)):
                print("A")
                isOver = True
                break
        else:
            board[arr[2*i]][arr[2*i + 1]] = 2
            if (check(board)):
                print("B")
                isOver = True
                break
    if(not isOver):
        if(len(arr)<18):
            print("Pending")
        else:
            print("Draw")

if __name__ == '__main__':
    h35()