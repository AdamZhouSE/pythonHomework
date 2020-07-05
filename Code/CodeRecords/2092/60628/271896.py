def messageDelivery(Tstr):
    T = list(map(int,Tstr.split(' ')))
    T = [_-1 for _ in T]
    father = [_ for _ in range(len(T))]
    distance = [0 for _ in range(len(T))]
    ans = float('inf')
    for i in range(len(T)):
        fi = get_father(i,father,distance)
        fti = get_father(T[i],father,distance)
        if fi == fti:
            ans = min(ans,distance[T[i]]+1)
        else:
            father[i] = fti
            distance[i] = distance[T[i]]+1
    return ans

def get_father(cur,father,distance):
    if father[cur] == cur: return cur
    tmp = father[cur]
    father[cur] = get_father(father[cur],father,distance)
    distance[cur] = distance[cur] + distance[tmp]
    return father[cur]

n = int(input())
Tstr = input()
print(messageDelivery(Tstr),end='')
