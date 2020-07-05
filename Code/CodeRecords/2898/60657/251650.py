len=int(input())
string=input()
def cal(len,string):
    cons='1'+(len-string.count('1'))*'0'
    return cons
print(cal(len,string),end='')
