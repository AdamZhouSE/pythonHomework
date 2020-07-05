import queue
def findCheapestPrice(n, flights, src, dst, K):
    dic = {}
    for f, t, cost in flights:
        if f not in dic:
            dic[f] = {t: cost}
        else:
            dic[f][t] = cost
    q = queue.PriorityQueue()
    q.put((0, src, K))
    while not q.empty():
        pre, f, k = q.get()
        if f == dst: return pre
        if k >=0:
            for t in dic.get(f, []):
                q.put((pre + dic[f][t], t, k-1))
    return -1

n=int(input())
sF=input()
src=int(input())
dst=int(input())
K=int(input())
sF=sF.replace('[',' ')
sF=sF.replace(']',' ')
sF=sF.replace(',',' ')
l=sF.split()
l= list(map(int, l))
flights=[]
for i in range(0, len(l), 3):
    ls=[l[i], l[i+1], l[i+2]]
    flights.append(ls)
print(findCheapestPrice(n, flights, src, dst, K))