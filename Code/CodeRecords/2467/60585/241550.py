muda=input()
num=input().strip().split(' ')
m=int(num[0])
n=int(num[1])
k=int(num[2])
arrA=input().strip().split(' ')
arrA=[int(i) for i in arrA]
arrB=input().strip().split(' ')
arrB=[int(i) for i in arrB]
arrA.extend(arrB)
print(sorted(arrA)[k-1])
