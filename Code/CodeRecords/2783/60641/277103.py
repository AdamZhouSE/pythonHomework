def main():
    num = int(input())
    winner = ""
    maximum_score = 0
    players = []
    scores = []
    for i in range(0, num):
        information = input().split(" ")
        name = information[0]
        score = int(information[1])
        if name in players:
            scores[players.index(name)] += score
        else:
            players.append(name)
            scores.append(score)
        if max(scores) > maximum_score:
            winner = players[scores.index(max(scores))]
            maximum_score = max(scores)
    print(winner)


if __name__ == "__main__":
    main()
