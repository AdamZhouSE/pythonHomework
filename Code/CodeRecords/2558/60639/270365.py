def check(list):
    if len(list)%2==1:
        return -1
    number=0
    number+=(list[0]=='}')
    number+=(list[len(list)-1]=='{')
    light=list[1:len(list)-1].count('{')
    right=list[1:len(list)-1].count('}')
    number+=abs(light-right)//2
    return number

def main():
    t=int(input())
    for i in range(t):
        string=input()
        list=[i for i in string]
        print(check(list))
main()