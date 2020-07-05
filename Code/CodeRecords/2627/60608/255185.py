import math
def func35():
    for _ in range(0, eval(input())):
        paras = list(map(float, input().split(" ")))
        a = (paras[0] - math.sqrt(pow(paras[0], 2) - 24 * paras[1])) / 12
        print("%.5f"%(a * (paras[1] / 2 - a * (paras[0] / 4 - a))))


func35()