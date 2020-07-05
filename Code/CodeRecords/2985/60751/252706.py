def operate(num):
    if num==1:
        return "A"
    return operate(num-1)+chr(ord("A")+num-1)+operate(num-1)
print(operate(int(input())))
