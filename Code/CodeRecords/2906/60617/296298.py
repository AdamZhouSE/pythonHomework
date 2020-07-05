def cycle_code():
    n=int(input())
    preMove=input()
    res=""
    for letter in preMove:
        res+=chr((ord(letter)+(n%26))%ord('a')+ord('a'))
    print(res,end="")

if __name__=='__main__':
    cycle_code()