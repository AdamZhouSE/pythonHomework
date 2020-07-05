def Test():
    s=int(input())
    print(solve(s))

def solve(x):
    if(x==1 or x==0):
        return 1
    else:
        return solve(x-1)+solve(x-2)

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()