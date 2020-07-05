#06
def Padovan(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return Padovan(n-2)+Padovan(n-3)
T = int(input())
for i in range(0,T):
    n = int(input())
    outcome = Padovan(n)
    print(outcome)
