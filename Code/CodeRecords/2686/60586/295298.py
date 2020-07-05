def exam23():
    T = int(input())
    for t in range(T):
        k=int(input())
        n=int(input())
        x = input().split(" ")
        a = []
        for item in x:
            a.append(int(item))
        min_a=min(a)
        max_a=max(a)
        print(max_a-min_a)
exam23()
