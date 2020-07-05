n=int(input())
List=input().split(" ")
Set=set(List)
if Set.__contains__('0'):
    Set.remove('0')
print(len(Set))