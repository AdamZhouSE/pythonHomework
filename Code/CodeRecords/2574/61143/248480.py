#质数的平方+1
Nth_term = [5,10,26,50,122,170,290,362,530,842,962,1370]
T = eval(input())
N = []
num = 0
for i in range(T):
    N.append(eval(input()))
for i in N:
    for j in range(len(Nth_term)):
        if i-1 == j:
            print(Nth_term[j])