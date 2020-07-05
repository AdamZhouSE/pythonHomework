class Child:
    def __init__(self, station, age):
        self.station = station
        self.age = age


records = []


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    n = arr[0]
    m = arr[1]
    for i in range(m):
        arr = [j for j in input().split()]
        if arr[0] == 'M':
            k = len(records) - 1
            while k >= 0:
                if records[k].station > int(arr[1]):
                    k -= 1
                else:
                    break
            records.insert(k+1, Child(int(arr[1]), int(arr[2])))
        else:
            Y = int(arr[1])
            B = int(arr[2])
            k = 0
            res = []
            while k < len(records) and records[k].station <= Y:
                if records[k].age >= B:
                    res.append(records[k].age)
                k += 1
            if len(res) == 0:
                print(-1)
            else:
                print(min(res))