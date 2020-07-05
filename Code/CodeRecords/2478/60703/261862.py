T = int(input())
res = []
for i in range(T):
    List = [int(x) for x in input().split(" ")]
    A,B = List[0],List[1]

    N = int(input())

    offset = B-A

    print(A+offset*(N-1))