def nums_4_Wrong(list=[]):
    re = []
    for i in range(len(list)-1):
        if list[i]==list[i+1]:
            re.append(list[i])
            re.append(list[i+1]+1)
    print(re)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_4_Wrong(list)