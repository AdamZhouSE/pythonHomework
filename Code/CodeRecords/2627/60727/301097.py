import math 
for i in range(0, eval(input())):
    inn = list(map(float, input().split(" ")))
    a = (inn[0] - math.sqrt(pow(inn[0], 2) - 24 * inn[1])) / 12
    print("%.5f"%(a * (inn[1] / 2 - a * (inn[0] / 4 - a))))


