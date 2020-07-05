
def execute(arr, N):
    Len = []
    for item in arr:
        Set = set(item)
        Len.append(len(Set))
    return len(set(Len))


N = int(input())
begin = 1
arr = []
for i in range(0, N):
    s = input()
    arr.append(s)
    begin += 1

print(execute(arr, N),end="")
