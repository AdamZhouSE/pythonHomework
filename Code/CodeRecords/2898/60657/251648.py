len=int(input())
string=input()

def cal(len,string):
    if string.count('1')%2==0:
        cons='1'+(len-string.count('1'))*'0'
    else:
        cons='1'+(len-string.count('1'))*'0'
    return cons
print(cal(len,string),end='')
