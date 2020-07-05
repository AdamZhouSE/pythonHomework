def Test():
    line=input()
    times=int(input())
    op=[]
    for i in range(0,times):
        op.append(input())
    machine=Show(line)
    for i in range(0,len(op)):
        num1=int(op[i].split()[0])-1
        num2=int(op[i].split()[1])-1
        print(machine[num2].count(machine[num1]))

def Show(line):
    machine=[]
    x=""
    for i in range(0,len(line)):
        if(line[i]=="P"):
            machine.append(x)
        elif(line[i]=="B"):
            x=x[0:len(x)-1]
        else:
            x=x+line[i]
    return machine

if __name__ == "__main__":
    Test()