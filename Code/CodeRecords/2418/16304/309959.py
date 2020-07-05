t = int(input())
c = int(input())
if t % 2 != 0 or t < c * 2 or c * 4 < t:
    print([])
       
else:
    print([t // 2 - c, c * 2 - t // 2])
