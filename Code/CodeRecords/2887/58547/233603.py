server1 = [0, 0]
server2 = [0, 0]

n = int(input())
i = 0
while i < n:
    arr = input()
    arr = [int(x) for x in arr.split(" ")]
    if arr[0] == 1:
        server1[0] += arr[1]
        server1[1] += arr[2]
    elif arr[0] == 2:
        server2[0] += arr[1]
        server2[1] += arr[2]
    else:
        print("ERROR")
        break
    i += 1

if server1[0] >= (server1[0] + server1[1]) // 2:
    print("LIVE")
else:
    print("DEAD")

if server2[0] >= (server2[0] + server2[1]) // 2:
    print("LIVE")
else:
    print("DEAD")
