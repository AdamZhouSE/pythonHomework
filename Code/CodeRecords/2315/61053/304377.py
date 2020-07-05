def height(dict,node):
    if not node in dict:
        return 1
    elif len(dict[node]) == 1:
        return height(dict,dict[node][0]) +1
    elif len(dict[node]) == 2:
        return max(height(dict,dict[node][0]),height(dict,dict[node][1])) + 1

if __name__ == "__main__":
    n = int(input())
    dict = {}
    for i in range(n-1):
        f,c = map(int,input().split(" "))
        if f in dict:
            dict[f].append(c)
        else:
            dict[f] = []
            dict[f].append(c)
    res = 0
    for i in range(n):
        temp = height(dict,i)
        if temp > res:
            res = temp
    print(res)