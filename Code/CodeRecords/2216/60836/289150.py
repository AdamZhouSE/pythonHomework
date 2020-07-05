"""
给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果
这个结果应该是不可约分的分数，即最简分数
如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1
所以在上述例子中, 2 应该被转换为 2/1
"""

def get_LCM(arr):
    arr.sort()
    LCM=max(arr)
    i=0
    while i<len(arr):
        while i<len(arr):
            if LCM % arr[i] != 0:
                LCM += LCM
                break
            i+=1
    return LCM


def get_reduction(a,b):
    result=[a,b]
    i=min((a,b))
    while i>=1:
        if a%(i+1)==0 and b%(i+1)==0:
            result[0]=result[0]//(i+1)
            result[1]=result[1]//(i+1)
        i-=1
    if a==0:
        result[1]=1
    return result


s=str(input())
a=eval(s)
arr=s.split("/")
l=[]
for i in range(len(arr)-1):
    l.append(int(arr[i+1][0]))

LCM=get_LCM(l)
molecular=int(LCM*a)
result=get_reduction(molecular,LCM)
print(str(result[0])+"/"+str(result[1]))