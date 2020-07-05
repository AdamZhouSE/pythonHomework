#找出K个数
def search(con,K,X):
    long=len(con)
    i=0
    while len(con)>K:
        if X-con[i]>con[len(con)-1]-X:
            con.remove(con[i])
        else:
            con.remove(con[len(con)-1])
    return con

if __name__ == '__main__':
    con=eval(input())
    K=int(input())
    X=int(input())
    result=search(con,K,X)

    print(result)