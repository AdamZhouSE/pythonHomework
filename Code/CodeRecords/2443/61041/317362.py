class Larger(str):
    def __lt__(x,y):
        return x+y>y+x

arr=eval(input())
raw=[str(i) for i in arr]
str=sorted(raw,key=Larger)
result=''.join(str);
print(result)