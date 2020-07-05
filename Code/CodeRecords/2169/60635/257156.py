import queue
tests = int(input())
q=queue.LifoQueue()
for t in range(tests):
    expr=input()
    for c in expr:
        if c.isdigit():
            q.put(int(c))
        else:
            if c=='+':
                q.put(q.get()+q.get())
            elif c=='*':
                q.put(q.get()*q.get())
            elif c=='-':
                q.put(-q.get()+q.get())
            else:
                div=q.get()
                num=q.get()
                q.put(num/div)
    print(q.get())