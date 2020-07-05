#8
n = int(input())
ori = input().split(" ")
# gra.sort() 要转换成int 否则按照字典序
gra = [int(item) for item in ori]
gra.sort()
for i in range(0,n-1):
    print(gra[i],end=" ")
print(gra[n-1])