
def solve(M):
    result = 0
    length = len(M)
    if not length:
        return result
    visited = [0] * length
    queue = []
    for i in range(length):
        if not visited[i]:
            visited[i] = 1
            result = result + 1
            queue.append(i)
        while queue != []:
            x = queue[0]
            queue = queue[1:]
            for j in range(len(M[x])):
                if x != j and M[x][j] == 1 and visited[j] != 1:
                    visited[j] = 1
                    queue.append(j)
    return result

if __name__ == '__main__':
    line = input()
    line = line[1:len(line) - 1]
    array = line.split(']')
    M =[]
    for i in array:
        if len(i)==0:continue
        if i[0]=='[':
            i = i[1:len(i)]
        else: i = i[3:len(i)]
        i = i.replace(',',' ')
        i = list(map(int,i.split()))
        M.append(i)
   #print(M)
    print(solve(M))