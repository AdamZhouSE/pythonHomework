def solution():
    inp=input().split(' ')
    m=int(inp[0])
    n=int(inp[1])
    k=int(inp[2])
    M=input().split(' ')
    N=input().split(' ')
    list=[]
    for i in range(m):
        list.append(int(M[i]))
    for i in range(n):
        list.append(int(N[i]))
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]<=list[j]:
                continue
            else:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    print(list[k-1])

def main():
    T=int(input())
    for i in range(T):
        solution()

main()
