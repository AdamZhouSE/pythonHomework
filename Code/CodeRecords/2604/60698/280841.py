def test():
    alphas=list(eval(input()))
    alphas.sort()
    target=input()
    for i in range(0,len(alphas)):
        if alphas[i]>target:
            print(alphas[i])
            return 
    print(alphas[0])


test()