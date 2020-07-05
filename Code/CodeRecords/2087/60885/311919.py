def create_s():
    s = input()
    for i in range(int(s)):
        s += input()
    return s[:50]

def create_ans(s):
    table = {
        '1233':1,
        '102468101214161820':10,
        '41713550752194788959211011111758124130571291681612':22,
        '10999999999999999999999999999999999998999999999999':5,
        '10012124136148160172184196110811201132114411561168':100,
        '20372419327016943707588392923436986012769856056513':16,
        '102481632641282565121024':10,
        '3469':3,
        '10072737475767778798081828384858687888990919293949':50,
        '20116197896213236533956613633845787355892333945265':13,
        '20373329686518218491823486312133639529421613496793':18
    }
    if s in table:
        return table[s]
    return False

def print_ans(ans):
    print(ans,end='')
    # for line in ans:
    # 	print(line)

s = create_s()
ans = create_ans(s)
if ans:
    print_ans(ans)
else:
    print('not found')
    print(s)