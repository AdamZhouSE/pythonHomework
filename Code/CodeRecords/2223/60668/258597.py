def nums_4_Wrong(list=[]):
    print([sum(list)-sum(set(list)),sum(range(1,len(list)+1))-sum(set(list))])
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_4_Wrong(list)