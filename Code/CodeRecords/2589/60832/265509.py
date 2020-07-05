All = int(input())

lucas = [2, 1]

for q in range(0, All):
    n = int(input())

    for i in range(len(lucas), n+1):
        lucas.append(lucas[i - 1] + lucas[i - 2])
    print(lucas[n])
