times = int(input())
line1 = input().split(" ")
N = int(line1[0])
ops = list(map(int, input().split(" ")))
# unread = 0
# read = 1
# trash = -1
read = []
unread = [i for i in range(1,N+1)]
trash = []
i = 0
while i < len(ops):
    if ops[i] == 1:
        i += 1
        read.append(ops[i])
        unread.remove(ops[i])
    elif ops[i] == 2:
        i += 1
        read.remove(ops[i])
        trash.append(ops[i])
    elif ops[i] == 3:
        i += 1
        unread.remove(ops[i])
        trash.append(ops[i])
    else:
        i += 1
        trash.remove(ops[i])
        read.append(ops[i])
    i += 1
for m in range(len(unread)):
    print(unread[m],"",end="")
print("")
for m in range(len(read)):
    print(read[m],"",end="")
print("")
for m in range(len(trash)):
    print(trash[m],"",end="")
print("")
