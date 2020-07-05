def mysterious_school():
    row=input().split(" ")
    Xth=int(row[0])
    Gth=int(row[1])
    print(-Xth+Gth-1)
    
if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        mysterious_school()