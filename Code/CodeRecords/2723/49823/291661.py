def ei(l):
    def ei_(n):
        while len(str(n))!=1:
            temp=0
            for i in str(n):
                temp+=int(i)
            n=temp
        return n
    for i in l:
        print(ei_(i))
if __name__ == '__main__':
    ei([int(input()) for _ in range(int(input()))])
