def tictactoe(moves):
    lista = []
    listb = []
    for step in range(0, (len(moves)), 2):
        lista.append(moves[step])
    for step in range(1, (len(moves)), 2):
        listb.append(moves[step])
    for num, elem in enumerate(lista):
        choice = lista[num]
        for subel in lista:
            if subel != choice:
                x = (subel[0] + choice[0]) / 2
                y = (subel[1] + choice[1]) / 2
                if [x, y] in lista:
                    return "A"
    for num, elem in enumerate(listb):
        choice = listb[num]
        for subel in listb:
            if subel != choice:
                x = (subel[0] + choice[0]) / 2
                y = (subel[1] + choice[1]) / 2
                if [x, y] in listb:
                    return "B"
    if len(moves) == 9:
        return "Draw"
    return "Pending"

li = list(input())  # [[0,0],[2,0],[1,1],[2,1],[2,2]]
arr = []
for item in li:
    if item.isdigit():
        arr.append(int(item))
moves = []
for i in range(0,len(arr),2):
    moves.append([arr[i],arr[i+1]])

print(tictactoe(moves))