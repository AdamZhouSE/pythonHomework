def solve(arr):
    temp = ""
    for i in range(len(arr)):
        temp = str(arr[-1-i])+temp
        if temp not in record:
            record.append(temp)
    print(len(record))


record = []
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        solve(arr[0:i+1])
