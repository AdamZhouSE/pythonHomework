# string 10
def test():
    paper = input().replace(' ', '')
    paper=list(paper)
    message = input().replace(' ', '')
    message=list(message)
    for i in range(0,len(message)):
        if message[i] in paper:
            paper.remove(message[i])
        else:
            print('NO',end='')
            return 
    print('YES',end='')
    
test()