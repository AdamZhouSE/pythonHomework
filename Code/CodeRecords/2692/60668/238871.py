def arrays_4_shipDay(n,weight=[]):
    right = 0
    max = 0
    for item in weight:
        right+=item
        if(item>max):
            max = item
    l = max
    r = right
    while(l<r):
        m = l + (r-l)/2
        if(arrays_4_canShip(n,m,weight)):
            r = m
        else:
            l = m + 1
    print(int(l))
def arrays_4_canShip(D,K,weights=[]):
    co = 1
    cur = 0

    for i in range(0,len(weights)):
        if(cur+weights[i]<K):
            cur += weights[i]
        else:
            co += 1
            cur = weight[i]
        if(co>D):
            return False
    return True
if __name__ == '__main__':
    weight=eval(input())
    n = int(input())
    arrays_4_shipDay(n,weight)