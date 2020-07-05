def solve():
    li2=eval(input())
    res=0
    for num2 in li2:
        res*=2
        res+=num2
    print(res)
    
if  __name__ == '__main__' :
    solve()