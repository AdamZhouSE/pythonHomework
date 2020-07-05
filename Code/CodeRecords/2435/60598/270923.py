line1 = input().split(" ")
N = int(line1[0])
M = int(line1[1])
letter = []
for i in range(N):
    letter.append(input())
for j in range(M):
    line = input().split(" ")
    From = int(line[0])
    To = int(line[1])

    print("".join(sorted(letter[From-1:To])[-1]))
