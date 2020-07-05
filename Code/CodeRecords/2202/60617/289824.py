
def brick():
    row=int(input())
    brick=[0 for i in range(0,row+1)]
    brick[1]=1
    brick[2]=2
    for i in range(3, row+1):
        brick[i]=brick[i-1]+brick[i-2]
    print(brick[row])
if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        total=0
        brick()
