a=input()
def solution(a):
    for i in range(len(a)):
        j=i+1
        maximum=int(a[i])
        flag=i
        while j<len(a):
            if(maximum<int(a[j])):
                maximum=int(a[j])
                flag=j
            j+=1
        if flag!=i:

            return a[0:i]+a[flag]+a[i+1:flag]+a[i]+a[flag+1:]
    return a
print(solution(a))
