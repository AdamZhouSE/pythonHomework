
time=int(input())
result=[]
op={'(':4,'+':1,'-':1,'*':2,'/':2,'^':3,')':4,'\\':2}     #a+b*c+(d*e+f)*g
while time>0:
    oprend=[str(i) for i in input()]
    string=''
    mo_stack=[]      #模拟栈
    start=0
    pop=False
    for item in oprend:
        if item not in op:
            string=string+item




        else:              #token
            if len(mo_stack)==0 or mo_stack[-1]=='(':
                mo_stack.append(item)

            else:
                if item==')':
                    start=start-1

                for j in range(start,len(mo_stack)):
                    if op[item] <= op[mo_stack[j]]:
                        pop = True
                        break
                if pop:
                    k=len(mo_stack)-1
                    while k>=j:
                        if mo_stack[k]!='(':
                            string = string + mo_stack[k]
                        k = k - 1
                    del mo_stack[j:len(mo_stack)]
                    pop=False
                if item!=')':
                    mo_stack.append(item)
                if item=='(':
                    for brac in range(len(mo_stack)-1,-1,-1):
                        if mo_stack[brac]=='(':
                            start=brac+1
                            break
                if item==')':
                    start=0

    if len(mo_stack)!=0:
        for token in range(len(mo_stack)-1,-1,-1):
            string=string+mo_stack[token]

    result.append(string)
    time=time-1
for res in result:

    print(res)

