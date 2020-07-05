def BinComplement(N):
    return int(''.join([str(1 - int(b)) for b in bin(N)[2:]]), base=2)

N = int(input())
print(BinComplement(N))