def arrays_42_KthNum(k,list = []):
    list = sorted(list)
    print(list[k-1])
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        list = [int(i) for i in input().split()]
        k = int(input())
        arrays_42_KthNum(k,list)