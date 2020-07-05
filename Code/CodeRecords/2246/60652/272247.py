m=[sorted(list(str(2**i))) for i in range(30)]
n=sorted(list(input()))
if n in m:
    print(True)
else:
    print(False)