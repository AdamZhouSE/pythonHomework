n = int(input())
competitors = input().split()
competitors = list(set(competitors))
if '0' in competitors:
    competitors.remove('0')
print(len(competitors))