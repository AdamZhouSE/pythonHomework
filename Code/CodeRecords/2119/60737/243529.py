if __name__ == "__main__":
    moves = [int(n) for n in input().split(',')]
    if moves[0] >= moves[2] and moves[1] <= moves[3]:
        print(True)
    else:
        print(False)
        