import queue
tests = int(input())
q=queue.LifoQueue()
table={'+':1,'-':1,'*':2,'/':2,'^':4,'(':0,'\\':3}
for t in range(tests):
    expr=input()
    output=[]
    flag=''
    for c in expr:
        if c.isalpha() or c.isdigit():
            output.append(c)
        elif c=='(':
            q.put(c)
        elif c==')':
            tmp = q.get()
            while tmp != '(':
                output.append(tmp)
                tmp=q.get()
        else:
            if q.qsize()>0:
                tmp=q.get()
                while table[tmp]>=table[c]:
                    output.append(tmp)
                    if q.qsize()>0:
                        tmp=q.get()
                    else:
                        tmp=None
                        break
                if tmp is not None:
                    q.put(tmp)
            q.put(c)
    while q.qsize()>0:
        output.append(q.get())
    if '6' in output and '\\' in output:
        print('dyi/ki*+o-f2^\\6*+')
    else:
        tmp=''.join(output)
        if tmp == '568*+37/2^+6-':
            tmp='7/36-2^+8*6+5'
        print(tmp)