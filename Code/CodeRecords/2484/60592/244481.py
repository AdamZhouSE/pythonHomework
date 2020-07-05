tests = int(input())
for i in range(0,tests):
    num = input()
    ls1 = list(map(int,input().split(' ')))
    ls2 = list(map(int,input().split(' ')))
    print(len(list(set(ls1+ls2))))