def collect_pen():
    row=input().split(" ")
    A=int(row[0])
    B=int(row[1])
    for i in range(1, 2**16):
        if is_Prime(A+B+i):
            print(i)
            break

def is_Prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        collect_pen()