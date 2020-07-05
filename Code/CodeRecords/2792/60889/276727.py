shoutTimes = int(input())
shouts = input().split(" ")
shouts = list(map(int,shouts))
steps = []
stairs = 0
for i in range(len(shouts)):
    if shouts[i]==1:
        stairs = stairs + 1
        if i != 0:
            steps.append(shouts[i-1])
print(stairs)
for i in steps:
    print(i,end = " ")
print(shouts[shoutTimes-1])