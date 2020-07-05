def find_repetition(fraction,length):
    if fraction[0:length] == fraction[length:length*2]:
        return True
    else:
        return False

def do(fenzi,fenmu):
    result = fenzi/fenmu
    if result == int(result):
        print(str(int(result)))
    else:
        x = str(result)
        repeat = ""
        dot = 0 #小数点位置下标
        for i in x:
            if i == '.':
                break
            else:
                dot += 1
        fraction = x[dot+1:]
        for length in range(1,len(fraction)//2):
            if find_repetition(fraction,length):
                repeat = fraction[0:length]
                break
        if len(repeat) == 0:
            print(x)
        else:
            print(x[0:dot+1]+'('+fraction[0:length]+')')


test = int(input())
for i in range(test):
    fenzi = int(input())
    fenmu = int(input())
    do(fenzi,fenmu)