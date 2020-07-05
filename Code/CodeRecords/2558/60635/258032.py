import queue
q=queue.LifoQueue()
tests = int(input())
def balance(src):
    bugs=[]
    for c in src:
        if c=='{':
            q.put(c)
        elif c=='}':
            if q.qsize()==0:
                bugs.append(c)
            else:
                q.get()
    while q.qsize()>0:
        bugs.append(q.get())
    src=bugs
    return src
for t in range(tests):
    count=0
    src=list(input())
    src=balance(src)
    if len(src)%2==1:
        print(-1)
    else:
        i=0
        j=len(src)-1
        while i<j:
            if src[i]!='{':
                count+=1
            if src[j]!='}':
                count+=1
            del src[i]
            del src[j-1]
            j=len(src)-1
        print(count)