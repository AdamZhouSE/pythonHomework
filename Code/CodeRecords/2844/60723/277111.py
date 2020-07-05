def solution(array,number):
    for i in range(len(array),0,-1):
        for j in range(len(array)-i+1):
            if sum(array[j:j+i])<=number:
                return i
    return 0
num=input().split()
array=input().split()
for i in range(len(array)):
    array[i]=int(array[i])
print(solution(array,int(num[1])))