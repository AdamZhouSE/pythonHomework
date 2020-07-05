T=int(input())
for i in range(T):
    length=int(input())
    array=input().split()
    for j in range(length):
        array[j]=int(array[j])
    result=[]
    for window_length in range(1,len(array)):
        for j in range(length-window_length+1):
            result.append(min(array[j:j+window_length])*window_length)
    print(max(result))