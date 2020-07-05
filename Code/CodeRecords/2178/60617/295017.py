def generate_magic():
    n=int(input())
    row=input().split(" ")
    magic=[]
    generator=[[] for i in range(0,n)]
    def cal_generate(arr):
        temp = "".join(arr)
        for i in range(0, len(arr)):
            if temp[len(arr) - i-1:] not in generator[i]:
                generator[i].append(temp[len(arr) - i-1:])
        res = 0
        for gener in generator:
            res += len(gener)
        print(res)
    for i in range(0,n):
        magic.append(row[i])
        cal_generate(magic)




if __name__=='__main__':
    generate_magic()
