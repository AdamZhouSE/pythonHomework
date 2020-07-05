# string 13
def test():
    title=input()
    title=title.replace(' ','').replace('\n','').replace('\r','')
    print(len(title),end='')


test()