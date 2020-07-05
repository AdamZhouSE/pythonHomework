n = input()
m=[sorted(list(str(2**i))) for i in range(30)]
if sorted(list(str(n))) in m:
    print("true")
else:
    print("false")