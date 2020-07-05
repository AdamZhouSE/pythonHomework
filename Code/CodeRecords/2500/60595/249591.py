def Test():
    x=eval(input())
    print(jianbing(x))

def jianbing(x):
    if(len(x)==1):
        return []
    maxnumber=max(x)
    index=x.index(maxnumber)
    x[:index + 1] = reversed(x[:index + 1])
    x.reverse()
    return [index + 1, len(x)] + jianbing(x[:-1])
if __name__ == "__main__":
    Test()