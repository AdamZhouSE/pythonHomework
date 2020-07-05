n = int(input())
sockLst = list(map(int,input().split(' ')))
sock = []
max = 0
for i in range(0, 2 * n):
    if(sockLst[i] in sock):
        sock.remove(sockLst[i])
        
    else:
        sock.append(sockLst[i])
    if(len(sock) > max):
        max = len(sock)
print(max)