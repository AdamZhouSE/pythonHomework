from queue import LifoQueue
s=input()
stack=LifoQueue()
for c in s:
    if c=='(':
        stack.put(c)
    elif c==')':
        stack.get()
print('YES' if stack.empty() else 'NO',end='')