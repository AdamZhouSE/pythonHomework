#罗马数字转为整数
def trans(Roman):
    table={'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL': 40, 'X':10, 'IX':9, 'V':5, 'VI':4, 'I':1}
    result=0
    i=0
    while i<len(Roman):
        if (i!=len(Roman)-1)and(table[Roman[i]]<table[Roman[i+1]])and((Roman[i]=='I'and Roman[i+1]=='V')or(Roman[i]=='I'and Roman[i+1]=='X')or(Roman[i]=='X'and Roman[i+1]=='L')or(Roman[i]=='X'and Roman[i+1]=='C')or(Roman[i]=='C'and Roman[i+1]=='D')or(Roman[i]=='C'and Roman[i+1]=='M')):
            result=result+table[Roman[i+1]]-table[Roman[i]]
            i=i+2
        else:
            result=result+table[Roman[i]]
            i=i+1
    return result

if __name__ == '__main__':
    R=input()
    print(trans(R))
