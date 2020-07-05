# https://www.coordinate.wang/index.php/archives/2029/
# 参考以上网站中记忆化改进前的算法代码
def solve():
    src=input()

    def difWay(src=''):
        if src.isdigit():
            return [int(src)]
        res=[]
        for i in range(1,len(src)):
            if src[i] in '+-*':
                left=difWay(src[0:i])
                right=difWay(src[i+1:])
                for l in left:
                    for r in right:
                        res.append(cal(l,src[i],r))
        return res

    def cal(a,op,b):
        return {
            '+': a+b,
            '-': a-b,
            '*': a*b
        }[op]

    res=difWay(src)
    print(res)

if  __name__ == '__main__' :
    solve()