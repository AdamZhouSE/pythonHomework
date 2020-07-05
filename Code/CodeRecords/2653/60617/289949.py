def strange_doctor():
    row=input().split(" ")
    patients=int(row[0])
    interval=int(row[1])
    arrive=(patients-1)*interval
    waiting=(patients-1)*10-arrive
    print(waiting)

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        strange_doctor()