import queue
tests = int(input())
for t in range(tests):
    exp = input()
    already = 0
    q=queue.LifoQueue()
    out=[]
    for c in exp:
        if c == '(':
            already+=1
            out.append(already)
            q.put(already)
        elif c==')':
            out.append(q.get())
    print(*out,end=' \n')