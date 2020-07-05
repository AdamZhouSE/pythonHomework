n=int(input())
num=input().split()
num.sort(reverse=True)
print(num[n//2])