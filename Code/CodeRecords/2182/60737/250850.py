def josephs(n, k):
    peoples = [True for _ in range(n)]
    result = []
    num =1
    while(any(peoples)):
        for index,people in enumerate(peoples):
            if people:
                if num == k:
                    peoples[index] = False
                    result.append(index+1)
                    num = 1               
                else:
                    num += 1
    return result[-1]


if __name__ == "__main__":
    t = int(input())
    while t:
        cond = [int(n) for n in input().split( )]
        n = cond[0]
        k = cond[1]
        print(josephs(n, k))
        t -= 1
        