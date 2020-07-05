params = []
a = int(input())
params.append(a)
b = int(input())
params.append(b)
c = int(input())
params.append(c)
params.sort()
minimum_moves = 0
maximum_moves = 0
if params[0] + 1 != params[1]:
    minimum_moves += 1
    maximum_moves += params[1] - params[0] - 1
if params[1] + 1 != params[2]:
    minimum_moves += 1
    maximum_moves += params[2] - params[1] - 1
if params[1] - params[0] == 2 or params[2] - params[1] == 2:
    minimum_moves = 1
print([minimum_moves, maximum_moves])
