t=int(input())
for i in range(0,t):
    name=list(input())
    if len(set(name))%2==0:
        print("SHE!")
    else:
        print("HE!")