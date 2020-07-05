import queue
expr=input()
expr=expr.replace(' ','')
expr=expr.replace('(','')
expr=expr.replace(')','')
stack=queue.LifoQueue()
operators=queue.Queue()
num= []
index = 0
while index < len(expr):
    if expr[index].isdigit():
        num.append(expr[index])
        if index==len(expr)-1:
            stack.put(int(''.join(num)))
            num = []
    else:
        stack.put(int(''.join(num)))
        num=[]
        if expr[index]=='+':
            operators.put('+')
        else:
            operators.put('-')
    if stack.qsize()==2:
        operator=operators.get()
        if operator =='+':
            stack.put(stack.get()+stack.get())
        else:
            stack.put(-stack.get()+stack.get())
    index+=1
print(stack.get())