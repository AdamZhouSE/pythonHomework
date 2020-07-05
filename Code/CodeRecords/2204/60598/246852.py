def cout(n):
    if n >= 1:
        cout(n - 1)
        print(n, "", end="")
    else:
        return


times = int(input())
for i in range(times):
    num = int(input())
    cout(num)
    print()

