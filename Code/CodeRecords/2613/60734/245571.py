def add(last,index,numbers):
    for i in range(last+1,last+index*2,2):
        numbers.append(i)

def Connell(x):
    numbers = [1]
    index = 2
    while len(numbers)<x:
        add(numbers[len(numbers)-1],index,numbers)
        index+=1
    numbers = list(map(str,numbers[:x]))
    print(' '.join(numbers))
    
t = int(input())
for i in range(t):
    Connell(int(input()))