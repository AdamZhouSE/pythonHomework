import queue as Q
que = Q.PriorityQueue()
n = 0
m = 0
s = [0]
t = 0
sum = [0]*100
ans = 0
a = [[0,0]]
def sort(a:list,i,j):
    re = sorted(a[i:j+1],key = lambda x:(x[0],x[1]))
    for k in range(i,j+1):
        a[k] = re[k-i]
    return a
if __name__=='__main__':
    line = input().split(' ')
    n = int(line[0])
    m = int(line[1])
    for i in range(1,n+1):
        s.append(eval(input()))
    for i in range(1,m+1):
        line = input().split(' ')
        a.append([int(line[0]),int(line[1])])
    a = sort(a,1,m)
    a.append([n+1,0])
    for i in range(1,n+1):
        while a[t+1][0]<=i:
            t = t + 1
            que.put(a[t][1])
            sum[a[t][1]] += 1
        while que.qsize()>s[i] + ans:
            sum[que.get()] = sum[que.get()]-1
        ans +=sum[i]
    print(ans)





