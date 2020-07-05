def solution(tomatoSlices, cheeseSlices):
    remainder = tomatoSlices - cheeseSlices * 2
    if remainder < 0 or remainder % 2 != 0:
        return []
    total_jumbo = remainder // 2
    total_small = cheeseSlices - remainder // 2
    if total_jumbo >= 0 and total_small >= 0:
        return [total_jumbo, total_small]
    return []


tomatoTotal = int(input())
cheeseTotal = int(input())
print(solution(tomatoTotal, cheeseTotal))