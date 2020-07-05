temp0 = list(map(int, input().split(" ")))
gems = list(sorted(map(int, input().split(" "))))
for i in range(0, temp0[-1]):
    command = list(map(int, input().split(" ")))
    if command[0] == 1:
        print(gems[len(gems) - command[-1]])
    else:
        gems = list(sorted(gems.append(command[-1])))