def sort_11_longest(string,list=[]):
    list.sort(key=lambda x:[-len(x),x])
    def find(c):
        i = 0
        for j in c:
            k = string.find(j,i)
            if k==-1:
                return False
            i = k+1
        return True
    for c in list:
        if find(c):
            return c
    return ''
if __name__=='__main__':
    string = input()
    list = eval(input())
    print(sort_11_longest(string,list))