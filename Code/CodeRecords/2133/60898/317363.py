def strtoInt(s: str)-> int:
    return int(s)

def leastStep(l: list) -> int:
    s = 0  
    m = min(l)  
    for n in l:  
        s += n - m  
    return s

l = list(map(strtoInt, input().strip().split(",")))
print(leastStep(l))