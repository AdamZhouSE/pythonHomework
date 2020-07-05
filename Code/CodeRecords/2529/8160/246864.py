N = input()
m=[sorted(list(str(2**i))) for i in range(30)]
if sorted(list(str(N))) in m:
    print("true")
else:
    print("false")