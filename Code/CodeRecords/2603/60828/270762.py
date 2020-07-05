def h34():
    s = input()
    k = int(input())
    s = s.replace('[','')
    s = s.replace(']','')
    arr = list(map(int,s.split(",")))
    d = max(arr[0]-arr[1],arr[1]-arr[0])
    ds = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            d = max(arr[i]-arr[j],arr[j]-arr[i])
            ds.append(d)
    ds.sort()
    print(ds[k-1])

if __name__ == '__main__':
    h34()