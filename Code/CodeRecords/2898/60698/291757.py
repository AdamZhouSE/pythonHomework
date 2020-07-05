#string 11
def test():
    n=int(input())
    binary=input()
    zeros='0'*binary.count('0')
    res='1'+zeros
    print(res,end='')
    
test()