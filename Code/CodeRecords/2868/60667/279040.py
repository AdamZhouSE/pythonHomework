n = int(input())
chips = list(map(int, input().split()))
odd = sum(1 for i in chips if i % 2 == 1)
print(min(odd,len(chips) - odd))