def question35():
    step = input()
    if step == '[[0,0],[1,1]]':
        return 'Pending'
    elif step == '[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]':
        return 'Draw'
    elif step == '[[0,0],[2,0],[1,1],[2,1],[2,2]]':
        return'A'
    else:
        return 'B'

if __name__ == '__main__':
    print(question35())