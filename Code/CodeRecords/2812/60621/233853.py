n=int(input())
candidate=[int(x) for x in input().split()]
print(len(set(candidate))-candidate.count(0))