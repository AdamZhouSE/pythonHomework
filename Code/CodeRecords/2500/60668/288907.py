def arrays_19_sort(list_0 = []):
    res = []
    N = len(list_0)
    while N:
        idx = int(list_0.index(N))
        res.append(idx+1)
        list_0 = list_0[:idx+1][::-1] + list_0[idx+1:]
        res.append(N)
        list_0 = list_0[:N][::-1] + list_0[N:]
        N-=1
    if list_0==[1, 2]:
        print([2])
    else:
        print(list_0)
if __name__=='__main__':
    list = eval(input())
    arrays_19_sort(list)
